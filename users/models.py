from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=20, blank=True)
    holiday = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=False)
    ipaddress = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
