from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=20, unique=True)
    
    
    unapproved_files = models.ManyToManyField("files.File", related_name="classes_unap", blank=True)
    files = models.ManyToManyField("files.File", related_name="classes", blank=True)
    rejected_files = models.ManyToManyField("files.File", related_name="classes_reject", blank=True)
    
    def __str__(self):
        return self.name
    