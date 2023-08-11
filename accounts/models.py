from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    """ 
    The model class responsible for handling users information
    """
    first_name = None
    last_name = None
    name = models.TextField(max_length=50)
    phone = models.TextField(max_length=15)
    gender = models.TextField(max_length=5)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username