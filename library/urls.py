"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from libman import views as core_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.redir, name='redirect_view'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('login', auth_views.LoginView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('libramini', include('libman.urls')),
]
