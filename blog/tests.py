from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post, PostImages


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
        )


class PostModelTest(BlogTests):
    def test_post_model(self):
        post = Post.objects.create(
            title='This is a test post',
            content='Just testing the post model',
            author=self.user,
        )
        self.assertEqual(post.title, 'This is a test post')
        self.assertEqual(post.content, 'Just testing the post model')
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(str(post), 'This is a test post')
        