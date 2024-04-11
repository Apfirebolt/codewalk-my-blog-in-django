from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView, View
from .models import Post, PostImages, Experience, About
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.utils.crypto import get_random_string


class RegisterUser(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = 'home'

    def form_valid(self, form):
        # perform a action here
        user_obj = form.save(commit=False)
        user_obj.staff = False
        user_obj.admin = False
        user_obj.save()
        messages.add_message(self.request, messages.INFO, 'You have successfully registered, Please login to continue!')
        return HttpResponseRedirect(reverse('login'))


class LoginView(View):

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        # if email or password is empty, return error
        if not email or not password:
            messages.add_message(self.request, messages.ERROR, 'Email and password are required fields!')
            return HttpResponseRedirect(self.request.path_info)
        
        user = authenticate(username=email, password=password)
        if user is not None:
            messages.add_message(self.request, messages.INFO,
                                 'You have successfully logged in! Please continue to your dashboard!')
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(self.request, messages.ERROR, 'Failed to Login, please try again!')
            return HttpResponseRedirect(self.request.path_info)

    def get(self, request):
        return render(request, 'accounts/login.html', {})


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


class AboutView(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'about.html'

    def get_queryset(self):
        qs = About.objects.filter(author_id=self.request.user.id)
        return qs


class PostImageList(ListView):
    model = PostImages
    context_object_name = 'images'
    template_name = 'posts/post_images.html'

    def get_queryset(self):
        qs = PostImages.objects.filter(post__author_id=self.request.user.id)
        return qs