# Generated by Django 2.2.10 on 2020-03-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20200302_0345'),
        ('course', '0002_course_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='unapproved_files',
            field=models.ManyToManyField(blank=True, related_name='classes_unap', to='files.File'),
        ),
    ]