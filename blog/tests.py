from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post, PostImages, Experience, About, PostTag, Tag, Category


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='someemail@gmail.com',
            password='password'
        )


class CategoryModelTest(BlogTests):

    def test_category_model(self):
        category = Category.objects.create(
            name='This is a test category',
        )
        self.assertEqual(category.name, 'This is a test category')


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

    

class AboutModelTest(BlogTests):
    def test_about_model(self):
        about = About.objects.create(
            content='This is a test about',
            author=self.user,
        )
        self.assertEqual(about.content, 'This is a test about')
        self.assertEqual(about.author.username, 'testuser')



class ExperienceModelTest(BlogTests):
    def test_experience_model(self):
        experience = Experience.objects.create(
            company='Test Company',
            job_title='Test Job',
            author=self.user,
            description='This is a test experience',
        )
        self.assertEqual(experience.company, 'Test Company')
        self.assertEqual(experience.job_title, 'Test Job')
        self.assertEqual(experience.author.username, 'testuser')
        self.assertEqual(experience.description, 'This is a test experience')
        self.assertEqual(str(experience), 'Test Job at Test Company')


class TagModelTest(BlogTests):
    def test_tag_model(self):
        tag = Tag.objects.create(
            name='Test Tag',
        )
        self.assertEqual(tag.name, 'Test Tag')
        self.assertEqual(str(tag), 'Test Tag')


class PostTagModelTest(BlogTests):
    def test_post_tag_model(self):
        post = Post.objects.create(
            title='This is a test post',
            content='Just testing the post model',
            author=self.user,
        )
        tag = Tag.objects.create(
            name='Test Tag',
        )
        post_tag = PostTag.objects.create(
            post=post,
            tag=tag,
        )
        self.assertEqual(post_tag.post.title, 'This is a test post')
        self.assertEqual(post_tag.tag.name, 'Test Tag')
        self.assertEqual(str(post_tag), 'This is a test post - Test Tag')
        