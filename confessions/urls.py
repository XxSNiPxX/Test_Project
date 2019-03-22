from django.contrib import admin
from django.views.generic import ListView, DetailView
from django.urls import re_path
from confessions.models import ConfessionTable
from confessions.views import postConfessions

urlpatterns=[
    re_path(r'^$', postConfessions.as_view(), name='confession-enter')
 ]
