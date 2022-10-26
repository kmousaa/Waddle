""" Test of sign up view """
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from microblogs.forms import SignUpForm
from microblogs.forms import User
from .helpers import LogInTester

class SignUpViewTestCase(TestCase,LogInTester):

    """ unit tests """
    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username':'@thejanedoe',
            'email':'janedoe@example.org',
            'bio': 'The bio',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }

    def test_sign_up_url(self):
        self.assertEqual(self.url, '/sign_up/')


    def test_get_sign_up(self):
        # test path for sign up view is sign up
        response = self.client.get(self.url)
        # assertions about sign up view
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,SignUpForm))
        self.assertFalse(form.is_bound)

    def test_unsuccesful_get_sign_up(self):
        self.form_input['username'] = 'BAD_USERNAME'
        before_count = User.objects.count()
        response = self.client.post(self.url,self.form_input)
        after_count = User.objects.count()
        self.assertEqual(after_count,before_count)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,SignUpForm))
        self.assertTrue(form.is_bound)
        self.assertFalse(self._is_logged_in())



    def test_succesful_get_sign_up(self):
        before_count = User.objects.count()
        response = self.client.post(self.url,self.form_input, follow = True)
        after_count = User.objects.count()
        self.assertEqual(after_count,before_count+1)
        response_url = reverse('feed')
        self.assertRedirects(response,response_url,302,target_status_code = 200)
        self.assertTemplateUsed(response,'feed.html')

        user = User.objects.get(username = '@thejanedoe')
        self.assertEqual(user.first_name , 'Jane')
        self.assertEqual(user.last_name , 'Doe')
        self.assertEqual(user.username , '@thejanedoe')
        self.assertEqual(user.email , 'janedoe@example.org')
        self.assertEqual(user.bio , 'The bio')
        is_pass_correct = check_password('Password123',user.password)
        #password is stored using hashing
        self.assertTrue(is_pass_correct )
        self.assertTrue(self._is_logged_in())
