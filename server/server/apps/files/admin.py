from django.contrib import admin

from .models import File

# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)