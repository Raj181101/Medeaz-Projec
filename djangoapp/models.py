from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father = models.CharField(max_length=20)
    mother = models.CharField(max_length=20)
    brother = models.CharField(max_length=20)
    sister = models.CharField(max_length=20)

    def __str__(self):
        return f'self.user'