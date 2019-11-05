# encoding: utf-8
"""
@project = mysite
@file = urls
@author = ThinkPad
@create_time = 2019-10-3020:41
"""
from django.urls import path
from . import views


app_name = 'javbus'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]