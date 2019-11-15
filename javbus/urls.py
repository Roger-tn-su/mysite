# encoding: utf-8
"""
@project = mysite
@file = urls
@author = ThinkPad
@create_time = 2019-10-3020:41
"""
from django.urls import path,re_path,converters
from . import views
import re

app_name = 'javbus'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('<avnum>', views.ModelDetailView.as_view(), name='detail')
]