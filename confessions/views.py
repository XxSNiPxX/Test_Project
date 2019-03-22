from django.shortcuts import render,redirect
from .forms import ConfessionForm
from django.views import generic
from django.views.generic.edit import CreateView
from .models import ConfessionTable
from confessions.forms import ConfessionForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.http import HttpResponseRedirect



# Create your views here.

class postConfessions(CreateView):
    template_name = 'confessions/confessions.html'
    form_class = ConfessionForm
    success_url = ''
    context={'form':form_class}
    #def get(self,request):
     #   post=ConfessionTable.objects.all()
        #print(post)
       # args={'form':ConfessionTable,'posts':post}
      #  return render(request,self.template_name,args)
        # def get(self, request):
    #      form=ConfessionForm()
     #     return render(request,self.template_name,context)
    def form_valid(self,form):  
        template_name = 'confessions/confessions.html'
        form_class = ConfessionForm
        context={'form':form_class}
        form.save()
        #posts=ConfessionTable.objects.all()
        messages.success(self.request, "Confession Added")
        return HttpResponseRedirect('/confessions')
    def get(self,request):
        posts=ConfessionTable.objects.all()
        context={'form':ConfessionForm,'posts':posts}
        return render(request,self.template_name,context)
        


#self.get_context_data()