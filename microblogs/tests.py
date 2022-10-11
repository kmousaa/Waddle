from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import User


#Unit tests goes here

class UserModelTestCase(TestCase):

    #setup
    def setUp(self):
        self.user = User.objects.create_user(
            username = '@kmousaa',
            first_name = 'Karim',
            last_name = 'Mousa',
            email = 'karimmousa@example.com',
            password = 'Password123',
            bio = 'Hey, this is crazy!'
        )

    #tests username

    def test_valid_user(self):
        user = self.user
        # asserts if user is valid
        self._assert_user_is_valid()

    def test_username_cant_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()


    def test_username_can_be_30_char_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_31_char_long(self):
        self.user.username = '@' + 'x' * 20
        self._assert_user_is_valid()


    def test_username_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()


    def test_username_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_alphanum_must_contain_symbols_only_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_alphanum_must_contain_at_least_3_symbols_only_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_may_contain_num(self):
        self.user.username = '@johndoe2'
        self._assert_user_is_valid()


    def test_must_contain_only_at(self):
        self.user.username = '@@johndoe2'
        self._assert_user_is_invalid()

  # test fname
    def test_fname_cant_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_fname_dont_need_unique(self):
        second_user = self._create_second_user()
        self.user.first_name = second_user.first_name
        self._assert_user_is_valid()


    def test_fname_may_contain_50_char(self):
        self.user.first_name = 'x' * 50
        self._assert_user_is_valid()


    def test_fname_may_not_contain_over_50_char(self):
        self.user.first_name = 'x' * 51
        self._assert_user_is_invalid()



  # test lname

    def test_valid_user(self):
        user = self.user
        # asserts if user is valid
        self._assert_user_is_valid()

    def test_username_cant_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()


    def test_username_can_be_30_char_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_31_char_long(self):
        self.user.username = '@' + 'x' * 20
        self._assert_user_is_valid()


    def test_username_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()


    def test_username_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_alphanum_must_contain_symbols_only_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_alphanum_must_contain_at_least_3_symbols_only_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_may_contain_num(self):
        self.user.username = '@johndoe2'
        self._assert_user_is_valid()


    def test_must_contain_only_at(self):
        self.user.username = '@@johndoe2'
        self._assert_user_is_invalid()

  # test lname
    def test_lname_cant_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_lname_dont_need_unique(self):
        second_user = self._create_second_user()
        self.user.last_name = second_user.last_name
        self._assert_user_is_valid()


    def test_lname_may_contain_50_char(self):
        self.user.last_name = 'x' * 50
        self._assert_user_is_valid()


    def test_lname_may_not_contain_over_50_char(self):
        self.user.last_name = 'x' * 51
        self._assert_user_is_invalid()

   #test email
    def test_email_cant_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.email = second_user.email
        self._assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@example.com'
        self._assert_user_is_invalid()

    def test_email_must_at_symbol(self):
        self.user.email = 'karimmousa.example.com'
        self._assert_user_is_invalid()


    def test_email_must_contain_domain_name(self):
        self.user.email = 'karimmousa@.org'
        self._assert_user_is_invalid()

    def test_email_must_cotain_domain(self):
        self.user.email = 'karimmousa@example'
        self._assert_user_is_invalid()

    def test_email_must_contain_only_1_at(self):
        self.user.email = 'karimmousa@@example.org'
        self._assert_user_is_invalid()







   #test bio
    def test_bio_may_be_blank(self):
        self.user.bio  = ''
        self._assert_user_is_valid()

    def test_bio_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.bio = second_user.bio
        self._assert_user_is_valid()


    def test_lname_may_contain_520_char(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()


    def test_lname_may_not_contain_more_than_520_char(self):
        self.user.bio = 'x' * 521
        self._assert_user_is_invalid()










   #helper methods
    def _assert_user_is_valid(self):
        # asserts if user is valid
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        # asserts if user is invalid
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def _create_second_user(self):
        user = User.objects.create_user(
            username = '@jojofan2',
            first_name = 'Jane',
            last_name = 'Doe',
            email = 'janedoe@yahoo.com',
            password = 'JaneISCool',
            bio = 'This is janes profile'
        )
        return user
