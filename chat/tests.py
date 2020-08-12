from django.test import TestCase
from .models import Room, Post
from django.contrib.auth.models import User


class ChatTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name="Room 1")
        Room.objects.create(name="Room 2")
        User.objects.create_user('user1', password='userpass1')
        self.client.login(username='user1', password='userpass1')

    def test_chat_loads(self):
        response = self.client.get('/1', follow=True)
        self.assertEqual(200, response.status_code)
        response = self.client.get('/2', follow=True)
        self.assertEqual(200, response.status_code)

    def test_chat_get_posts(self):
        response = self.client.post('/get_posts', {'room_id':1, 'last_check':''}, follow=True)
        self.assertEqual(200, response.status_code)
        response = self.client.post('/get_posts', {'room_id':2, 'last_check':''}, follow=True)
        self.assertEqual(200, response.status_code)

    def test_chat_post_message(self):
        response = self.client.post('/post_message', {'room_id':1, 'message':'Test message'}, follow=True)
        self.assertEqual(200, response.status_code)
