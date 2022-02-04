from django.conf.urls import *
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path, re_path
urlpatterns = [
    path('' , views.index , name = 'index')
]

