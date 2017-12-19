from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from .views import home, board_topics
from .models import Board
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

class BoardTopicsTest(TestCase):
    def test_board_topics_view_contains_ink_back_to_home_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk':2})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

class NewTopicTests(TestCase):

    def SetUp(self):
        Board.object.create(name='django', description = 'Django Board')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)



    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)



    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEqual(view.func, new_topic)


    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk':1})
        board_topics_url = reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))