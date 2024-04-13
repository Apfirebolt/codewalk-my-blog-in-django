from django.test import TestCase
from blog.models import Tag
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_TAG_URL = reverse('api:tags-list')
DETAIL_TAG_URL = 'api:tags-detail'


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_tag(**params):
    """Create and return a new tag."""
    return Tag.objects.create(**params)

def detail_url(group_id):
    """Create and return a group detail URL."""
    return reverse('api:tags-detail', args=[group_id])


class TagTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )
        self.client.force_authenticate(user=self.user)

    
    def test_create_tag(self):
        """Test creating a new tag."""
        payload = {
            'name': 'Test Tag',
        }
        res = self.client.post(CREATE_TAG_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    
    def test_get_multiple_categories(self):
        """Test getting multiple categories."""

        self.client.post(CREATE_TAG_URL, {'name': 'Test Tag 1'})
        self.client.post(CREATE_TAG_URL, {'name': 'Test Tag 2'})

        res = self.client.get(CREATE_TAG_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    
    def test_get_single_tag(self):
        """Test getting a single tag."""

        tag = create_tag(name='Test Tag')
        res = self.client.get(detail_url(tag.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_delete_tag(self):
        """Test deleting a tag."""

        tag = create_tag(name='Test Tag')
        res = self.client.delete(detail_url(tag.id))

    
    def test_update_tag(self):
        """Test updating a tag."""

        tag = create_tag(name='Test Tag')
        payload = {
            'name': 'Updated Tag',
        }
        res = self.client.patch(detail_url(tag.id), payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], payload['name'])
    
    