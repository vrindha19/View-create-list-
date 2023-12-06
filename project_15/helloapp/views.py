# from django.shortcuts import render

# # Create your views here.
# from django.views.generic.edit import CreateView
# from .models import RegisterModel

# class registercreate(CreateView):
#       model=RegisterModel
#       fields=['name','username','email','password','confirmpassword']

#       template_name='register_form.html'


from django.views.generic.list import ListView
from.models import RegisterModel

class RegisterList(ListView):
    model=RegisterModel

    template_name='register_list.html'
    context_object_name='login_list'


