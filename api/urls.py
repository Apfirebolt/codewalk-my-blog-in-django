from django.urls import path
from django.urls import path, include
from .views import ListCustomUsersApiView, CreateCustomUserApiView, CustomTokenObtainPairView, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . views import ListCustomUsersApiView, CreateCustomUserApiView, CustomTokenObtainPairView, CategoryViewSet
    
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('register', CreateCustomUserApiView.as_view(), name='signup'),
    path('login', CustomTokenObtainPairView.as_view(), name='signin'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('users', ListCustomUsersApiView.as_view(), name='list-users'),
    path('', include(router.urls)),
]