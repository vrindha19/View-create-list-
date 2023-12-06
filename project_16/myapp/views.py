#  create view

# from django.shortcuts import render

# # Create your views here.
# from django.views.generic.edit import CreateView
# from .models import LoginModel

# class logincreate(CreateView):
    #  model=LoginModel

    #  fields=['name','password']

    #  template_name='login_form.html'

# list view


from django.views.generic.list import ListView
from.models import LoginModel

class LoginList(ListView):
    model=LoginModel

    template_name='login_formlist.html'
    context_object_name='login_list'





