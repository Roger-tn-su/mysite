# encoding: utf-8
"""
@project = mysite
@file = urls
@author = ThinkPad
@create_time = 2019-10-1119:04
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]