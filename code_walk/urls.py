"""code_walk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from code_walk import settings
from django.views.generic import TemplateView
import django.contrib.auth.views as AuthViews
from blog.views import ExperienceList, AboutView, RegisterUser, LoginView, UpdateAccountSettings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('about/', AboutView.as_view(), name='about'),
    path('experience/', ExperienceList.as_view(), name='experience'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', AuthViews.LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('update-account/', UpdateAccountSettings.as_view(), name='update-account'),
    path('blog/', include('blog.urls'), name='blog'),
    path('api/', include('api.urls'), name='api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
