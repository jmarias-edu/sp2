from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class gauthuser(AbstractUser):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    user_id = models.CharField(max_length=50)
    password = None