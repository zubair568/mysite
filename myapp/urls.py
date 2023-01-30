"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import theinclude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index , name='index'),
    path('login_user', views.login_user , name='login_user'),
    path('registration', views.registration , name='registration'),
    path('logout', views.logout, name='logout'),
    path("post_detail", views.post_detail, name='post_detail'),
    path('edit/<id>', views.edit, name="edit"),
    url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete")


]


