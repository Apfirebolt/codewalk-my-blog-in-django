from django.test import TestCase
from blog.models import Category
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_CATEGORY_URL = reverse('api:category-list')
DETAIL_CATEGORY_URL = 'api:category-detail'


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_category(**params):
    """Create and return a new category."""
    return Category.objects.create(**params)

def detail_url(group_id):
    """Create and return a group detail URL."""
    return reverse('api:category-detail', args=[group_id])


class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )
        self.client.force_authenticate(user=self.user)

    
    def test_create_category(self):
        """Test creating a new category."""
        payload = {
            'name': 'Test Category',
        }
        res = self.client.post(CREATE_CATEGORY_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    
    def test_get_multiple_categories(self):
        """Test getting multiple categories."""

        self.client.post(CREATE_CATEGORY_URL, {'name': 'Test Category 1'})
        self.client.post(CREATE_CATEGORY_URL, {'name': 'Test Category 2'})

        res = self.client.get(CREATE_CATEGORY_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    
    def test_get_single_category(self):
        """Test getting a single category."""

        category = create_category(name='Test Category')
        res = self.client.get(detail_url(category.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_delete_category(self):
        """Test deleting a category."""

        category = create_category(name='Test Category')
        res = self.client.delete(detail_url(category.id))

    
    def test_update_category(self):
        """Test updating a category."""

        category = create_category(name='Test Category')
        payload = {
            'name': 'Updated Category',
        }
        res = self.client.patch(detail_url(category.id), payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], payload['name'])
    
    