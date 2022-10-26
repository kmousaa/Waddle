from django import forms
from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User
from django.contrib.auth.hashers import check_password

class SignUpFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username':'@thejanedoe',
            'email':'janedoe@example.org',
            'bio': 'The bio',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }


    #Form accepts valid inout default_auto_field
    def test_valid_sign_up_form(self):
        form = SignUpForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    #Form has the nessesary fields
    def test_form_has_nessesary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email'] #email field displayed by EmailField
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('new_password', form.fields)
        new_pass_widget  = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_pass_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        new_pass_conf_widget  = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(new_pass_widget, forms.PasswordInput))

    def test_uses_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    # New password has correct format
    def test_password_has_uppcase(self):
        self.form_input['new_password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_has_lowcase(self):
        self.form_input['new_password'] = ' PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_have_nums(self):
        self.form_input['new_password'] = 'passwordABC'
        self.form_input['password_confirmation'] = 'passwordABC'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    #NEw password and password identical

    def test_pass_and_comf_identical(self):

        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())




    def test_form_must_save_correctly(self):
        form = SignUpForm(data = self.form_input)
        before_count = User.objects.count()
        form.save()
        after_count = User.objects.count()
        self.assertEqual(after_count,before_count+1)

        user = User.objects.get(username = '@thejanedoe')
        self.assertEqual(user.first_name , 'Jane')
        self.assertEqual(user.last_name , 'Doe')
        self.assertEqual(user.username , '@thejanedoe')
        self.assertEqual(user.email , 'janedoe@example.org')
        self.assertEqual(user.bio , 'The bio')
        is_pass_correct = check_password('Password123',user.password)
        #password is stored using hashing
        self.assertTrue(is_pass_correct )
