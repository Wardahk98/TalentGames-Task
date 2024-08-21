from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RegisterUser(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
