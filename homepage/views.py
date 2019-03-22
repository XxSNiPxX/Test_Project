
from django.shortcuts import render,redirect

from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib import messages
# Create your views here.
class IndexView(TemplateView):
    def get(self,request):
        return render(request,'homepage/index.html')