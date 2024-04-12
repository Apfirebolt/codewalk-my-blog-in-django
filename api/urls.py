from django.urls import path
from django.urls import path, include
from .views import ListCustomUsersApiView, CreateCustomUserApiView, CustomTokenObtainPairView, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . views import ListCustomUsersApiView, CreateCustomUserApiView, CustomTokenObtainPairView, CategoryViewSet, AboutViewSet \
    , ExperienceViewSet, ListPostApiView, CreatePostApiView, PostTagViewSet
    
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'about', AboutViewSet, basename='about')
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'post-tags', PostTagViewSet, basename='post-tags')


urlpatterns = [
    path('register', CreateCustomUserApiView.as_view(), name='signup'),
    path('login', CustomTokenObtainPairView.as_view(), name='signin'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('users', ListCustomUsersApiView.as_view(), name='list-users'),
    path('', include(router.urls)),
    path('posts', ListPostApiView.as_view(), name='list-posts'),
    path('create-post', CreatePostApiView.as_view(), name='create-post'),
]