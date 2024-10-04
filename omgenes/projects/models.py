from django.db import models
from gauth.models import gauthuser



def fileDirectory(instance, filename):
    return "projects/user_{0}/{1}/{2}".format(instance.owner.id, instance.project.id, filename)

def fileDirectoryCalls(instance, filename):
    return "varcalls/user_{0}/{1}/{2}".format(instance.owner.id, instance.project.id, filename)

def folderCalls(instance):
    return "varcalls/user_{0}/{1}/".format(instance.owner.id, instance.id)

# File Test Upload
class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Variant Reads Classes

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


# Variant Calling Classes

# Class for creating filepath
class DirectoryPathField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 255)
        super().__init__(*args, **kwargs)
    
    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if not os.path.isdir(value):
            raise ValidationError(f"{value} is not a valid directory path")
        return value

# Class for files of Variant Call
class VariantCallProject(models.Model):
    name = models.CharField(max_length=50)
    referenceGenomeURL = models.URLField(max_length=256, null=True, blank=True, default=None)
    genomeURL = models.URLField(max_length=256, null=True, blank=True, default=None)
    vcfURL = models.URLField(max_length=256, null=True, blank=True, default=None)
    owner = models.ForeignKey(gauthuser, on_delete=models.CASCADE)
    folder = models.CharField(max_length=256, default='', editable=False)
    status = models.CharField(max_length=40, default="pending", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set the directory path when saving the instance
        self.folder = folderCalls(self)
        super().save(*args, **kwargs)

# Class for File Upload of Variant Call
class UploadedVariantCallProjectFile(models.Model):
    file = models.FileField(upload_to=fileDirectoryCalls)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(gauthuser, on_delete=models.CASCADE)
    project = models.ForeignKey(VariantCallProject, on_delete=models.CASCADE)