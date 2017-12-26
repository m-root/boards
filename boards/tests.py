from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .views import new_topics
from .views import home, board_topics
from .models import Board, Topic, Post


# Create your tests here.
# class HomeTest(TestCase):
#     def test_home_view_status_code(self):
#         url = reversed('home')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEqual(view.func, home)
#
# class BoardTopicTests(TestCase):
#     def setUp(self):
#         Board.objects.create(name='django', description='django bpard.')
#
#     def test_board_topics_view_success_status_code(self):
#         url = reverse('board_topics', kwargs={'pk':1})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_boards_view_not_found_status_code(self):
#         url = reversed('board_topics', kwargs = {'pk': 1})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)
#
#     def test_boards_topics_url_resolves_board_topics_view(self):
#         view = resolve('/boards1/1/')
#         self.assertEqual(view.func, board_topics)
#
# class HomeTests(TestCase):
#     def setUp(self):
#         self.board = Board.object.create(name = 'django', description = 'Django Board')
#         url = reverse('home')
#         self.response = self.client.get(url)
#
#     def test_home_view_status_code(self):
#         self.assertEqual(self.response.status_code, 200)
#
#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEqual(view.func, home)
#
#     def test_home_view_contains_link_to_topics_page(self):
#         board_topics_url = reverse('board_topic', kwargs={'pk': self.board.pk})
#         self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

# class BoardTopicsTest(TestCase):
#     def test_board_topics_view_contains_ink_back_to_home_page(self):
#         board_topics_url = reverse('board_topics', kwargs={'pk':2})
#         response = self.client.get(board_topics_url)
#         homepage_url = reverse('home')
#         self.assertContains(response, 'href="{0}"'.format(homepage_url))
#
# class NewTopicTests(TestCase):
#
#     def SetUp(self):
#         Board.object.create(name='django', description = 'Django Board')
#
#     def test_new_topic_view_success_status_code(self):
#         url = reverse('new_topic', kwargs={'pk':1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#
#
#     def test_new_topic_view_not_found_status_code(self):
#         url = reverse('new_topic', kwargs={'pk':99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)
#
#
#
#     def test_new_topic_url_resolves_new_topic_view(self):
#         view = resolve('/boards/1/new/')
#         self.assertEqual(view.func, new_topic)
#
#
#     def test_new_topic_view_contains_link_back_to_board_topics_view(self):
#         new_topic_url = reverse('new_topic', kwargs={'pk':1})
#         board_topics_url = reverse('board_topics', kwargs={'pk':1})
#         response = self.client.get(new_topic_url)
#         self.assertContains(response, 'href="{0}"'.format(board_topics_url))

class New_Topic_Test(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django Boards')
        User.objects.create_user(username='john', email='fafae@gmail.com', password='11123')

    def test_csrf(self):
        url = reverse('new_topics', kwargs={'pk':1})

        data = {
            'subject':'test title',
            'message':'Lorem Ipsum'
        }

        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behaviour is to show the form with validation errors

        '''

        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)


    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behaviour is to show the form with validation errors

        '''

        url = reverse('new_topic', kwargs={'pk':1})
        data = {
            'subject': ' ',
            'message': ' '
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Topic.objects.exists())
        # response = self.assertEqual(response.status_code)

class board_topic_stest(TestCase):
    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk':1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic' , kwargs={'pk':1})

        response = self.client.get(board_topics_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))

class NewTopicTests(TestCase):
    # ... other tests

    def test_contains_form(self):  # <- new test
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_invalid_post_data(self):  # <- updated this one
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
