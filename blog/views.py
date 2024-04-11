from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post, PostImages, Experience, About
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.utils.crypto import get_random_string


class DetailPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/detail_post.html'

    def get_object(self, queryset=None):
        currentObj = super(DetailPostView, self).get_object()
        if currentObj.created_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj
    

class PostList(ListView):
    model = Post
    template_name = 'posts/list_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = Post.objects.filter(author_id=self.request.user.id)
        return qs
    

class ExperienceList(ListView):
    model = Experience
    template_name = 'experience.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        qs = Experience.objects.filter(author_id=self.request.user.id)
        return qs


class AboutView(DetailView):
    model = About
    context_object_name = 'about'
    template_name = 'about.html'

    def get_object(self, queryset=None):
        currentObj = super(AboutView, self).get_object()
        if currentObj.author_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj
