from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from .views import signup
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm

class SignUpTest(TestCase):
    def test_signup_status_code(self):
        url= reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

class SuccessfulSignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username':'john',
            'username':'john@gmail.com',
            'password1':'1233333dsdse4',
            'password2':'1233333dsdse4',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        :return:
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a 'user' to its context,
        after a successful sign up.
        :return:
        '''

        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        :return:
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())



