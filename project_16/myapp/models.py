

#  create view  




# from django.db import models
  
# # declare a new model with a name "GeeksModel"
# class loginModel(models.Model):
 
#     # fields of the model
#    name = models.CharField(max_length = 200)
#    password = models.CharField(max_length = 200)
#    def __str__(self):
#         return self.name


# list view

from django.db import models

# Create your models here.
class LoginModel(models.Model):
   name=models.CharField(max_length = 200)
   password=models.CharField(max_length = 200)
   def __str__(self):
        return self.name
