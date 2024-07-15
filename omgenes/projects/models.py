from django.db import models
from gauth.models import gauthuser



def fileDirectory(instance, filename):
    return "projects/user_{0}/{1}/{2}".format(instance.owner.id, instance.project.id, filename)

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class VariantRead(models.Model):
    name = models.CharField(max_length=50)
    genomeURL = models.URLField(max_length=256, null=True, blank=True, default=None)
    variantURL = models.URLField(max_length=256, null=True, blank=True, default=None)
    owner = models.ForeignKey(gauthuser, on_delete=models.CASCADE)

class UploadedProjectFile(models.Model):
    file = models.FileField(upload_to=fileDirectory)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(gauthuser, on_delete=models.CASCADE)
    project = models.ForeignKey(VariantRead, on_delete=models.CASCADE)