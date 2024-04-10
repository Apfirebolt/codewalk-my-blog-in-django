from . views import DetailPostView, PostList
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('posts/<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('posts/', PostList.as_view(), name='list_post'),
]
