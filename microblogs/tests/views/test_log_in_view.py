""" Test of log in view """
from django.contrib import messages
from django.test import TestCase
from django.urls import reverse
from microblogs.forms import LogInForm
from microblogs.models import User
from microblogs.tests.helpers import LogInTester, reverse_with_next

class LogInViewTestCase(TestCase,LogInTester):

    fixtures = ['microblogs/tests/fixtures/default_user']

    def setUp(self):
        self.url = reverse('log_in')
        self.user = User.objects.get(username = "@johndoe")

        # self.user = User.objects.create_user('@johndoe',
        #     first_name = 'John',
        #     last_name = 'Doe',
        #     email = 'johndoe@example.org',
        #     bio = 'Hey, this is crazy!',
        #     password = 'Password123',
        #     is_active = True
        #
        # )

    def test_sign_up_url(self):
        self.assertEqual(self.url, '/log_in/')


    def test_get_log_in(self):
        response = self.client.get(self.url) #getting the log in view
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'log_in.html')
        form = response.context['form']
        next = response.context['next']
        self.assertTrue(isinstance(form,LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(next)
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list),0)



#test if we can get login view with a redirect parameter
    def test_get_log_in_with_redirect(self):
        destination_url = reverse('user_list')
        self.url = reverse_with_next('log_in', destination_url)
        response = self.client.get(self.url) #getting the log in view
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'log_in.html')
        form = response.context['form']
        next = response.context['next']
        self.assertTrue(isinstance(form,LogInForm))
        self.assertFalse(form.is_bound)
        self.assertEqual(next, destination_url)
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list),0)

    def test_unsuccessful_log_in(self):
        form_input = {'username' : '@johndoe', 'password' : 'WrongPassword123'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list),1)
        self.assertEqual(messages_list[0].level,messages.ERROR)

    def test_successful_log_in(self):
        form_input = {'username' : '@johndoe', 'password' : 'Password123'}
        response = self.client.post(self.url, form_input, follow = True)
        self.assertTrue(self._is_logged_in())
        response_url = reverse('feed')
        self.assertRedirects(response,response_url,302,target_status_code = 200)
        self.assertTemplateUsed(response,'feed.html')
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list),0)


    def test_valid_log_in_by_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        form_input = {'username' : '@johndoe', 'password' : 'Password123'}
        response = self.client.post(self.url, form_input, follow = True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'log_in.html')
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list),1)
        messages_list = list(response.context['messages'])
        self.assertEqual(messages_list[0].level,messages.ERROR)



    def test_get_log_in_with_redirect_when_logged_in(self):
        self.client.login(username = self.user.username, password="Password123")
        response = self.client.get(self.url,follow=True) #getting the log in view
        response_url = reverse('feed')
        self.assertRedirects(response,response_url,302,target_status_code = 200)
        self.assertTemplateUsed(response,'feed.html')

    def test_post_log_in_with_redirect_when_logged_in(self):
        self.client.login(username = self.user.username, password="Password123")
        form_input = {'username' : '@wrongjohndoe', 'password' : 'WrongPassword123'}
        response = self.client.post(self.url,form_input,follow=True) #getting the log in view
        response_url = reverse('feed')
        self.assertRedirects(response,response_url,302,target_status_code = 200)
        self.assertTemplateUsed(response,'feed.html')



    def test_successful_log_in_with_redirect(self):
        redirect_url = reverse('user_list')
        form_input = {'username' : '@johndoe', 'password' : 'Password123', 'next': redirect_url}
        response = self.client.post(self.url, form_input, follow = True)
        self.assertTrue(self._is_logged_in())
        self.assertRedirects(response,redirect_url,302,target_status_code = 200)
        self.assertTemplateUsed(response,'user_list.html')
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list),0)
