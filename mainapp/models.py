from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AccountsModel(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    checkbox = models.CharField(max_length=100)
    def __str__(self):
        return "%s :  %s : %s" % (self.checkbox, self.name, self.phonenumber)