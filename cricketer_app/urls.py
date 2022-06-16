"""cricket_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('all_cricketer', views.all_cricketer, name='all_cricketer'),
    path('add_cricketer', views.add_cricketer, name='add_cricketer'),
    path('remove_cricketer', views.remove_cricketer, name='remove_cricketer'),
    path('remove_cricketer/<int:cricketer_id>', views.remove_cricketer, name='remove_cricketer'),
    path('filter_cricketer', views.filter_cricketer, name='filter_cricketer')
]
