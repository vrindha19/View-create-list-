from django.db import models

# Create your models here.
# from django.db import models
  
# # declare a new model with a name "GeeksModel"
class RegisterModel(models.Model):
 
     # fields of the model
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    email=models.EmailField()
    password = models.CharField(max_length = 200)
    confirmpassword = models.CharField(max_length = 200)

    def __str__(self):
         return self.name
