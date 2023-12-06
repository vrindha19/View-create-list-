# from django.shortcuts import render

# # # Create your views here.

# # from django.shortcuts import render

# # # # Create your views here.
# from django.views.generic.edit import CreateView
# from .models import ForgotModel

# class forgotcreate(CreateView):
#       model=ForgotModel

#       fields=['Email']
#       template_name='forgot.html'
from django.views.generic.list import ListView
from.models import ForgotModel

class ForgotList(ListView):
    model=ForgotModel

    template_name='forgot list.html'
    context_object_name='forgot_list'