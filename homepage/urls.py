from django.contrib import admin
from django.views.generic import ListView, DetailView
from django.urls import re_path
from homepage.views import IndexView

urlpatterns=[
    re_path(r'^$', IndexView.as_view(),name='index')
 ]
