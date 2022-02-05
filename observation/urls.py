from django.conf.urls import *
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path, re_path
urlpatterns = [
    path('' , views.index , name = 'index'),
    path('fields' , views.fields , name = 'fields'),
    path('fields/' , views.fields , name = 'fields'),
    re_path(r'^fields/(?P<field_id>\d+)/$',views.field ,name = 'field')
]

