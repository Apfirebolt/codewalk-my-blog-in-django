from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from . serializers import  CustomUserSerializer, CustomTokenObtainPairSerializer, ListCustomUsersSerializer, AboutSerializer \
    , ExperienceSerializer, ListPostsSerializer, TagSerializer, PostTagSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import CustomUser
from rest_framework import viewsets
from .serializers import CategorySerializer
from blog.models import Category, About, Experience, Post, Tag, PostTag, PostImages



class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = []

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = []


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUsersSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    permission_classes = [IsAuthenticated]


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes = [IsAuthenticated]


class ListPostApiView(ListAPIView):
    serializer_class = ListPostsSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]


class CreatePostApiView(CreateAPIView):
    serializer_class = ListPostsSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDestroyPostApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ListPostsSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.author = request.user
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()
    
    def perform_update(self, serializer):
        serializer.save()
    
    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
    
    def get_object(self):
        obj = super().get_object()
        return obj
    

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]


class PostTagViewSet(viewsets.ModelViewSet):
    serializer_class = PostTagSerializer
    queryset = PostTag.objects.all()
    permission_classes = [IsAuthenticated]