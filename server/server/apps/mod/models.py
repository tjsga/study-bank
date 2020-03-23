from django.db import models

# Create your models here.

class Moderator(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, unique=True)
    admin = models.BooleanField(default=False)
    
    classes = models.ManyToManyField("course.Course", related_name="mods", blank=True)
    
    def __str__(self):
        return self.username