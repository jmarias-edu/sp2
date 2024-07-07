from django.db import models
from gauth.models import gauthuser

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class VariantRead(models.Model):
    name = models.CharField(max_length=50)
    genomeURL = models.URLField(max_length=256)
    variantURL = models.URLField(max_length=256)
    owner = models.ForeignKey(gauthuser, on_delete=models.CASCADE)