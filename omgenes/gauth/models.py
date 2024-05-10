from django.db import models

# Create your models here.
class gauthuser(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
