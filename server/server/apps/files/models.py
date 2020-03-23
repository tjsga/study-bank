from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from time import strftime

# Create your models here.
def gen_filename(instance, filename):
    return "upload_{0}_{1}_{2}.{3}".format(strftime('%Y-%m-%d-%H-%M%S'), uuid4(), slugify(instance.name), filename.split('.')[-1])

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    
    
    uploader = models.CharField(max_length=100)
    
    payload = models.FileField(blank=True, upload_to=gen_filename)
    
    def __str__(self):
        return self.name
