# Generated by Django 2.2.10 on 2020-03-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='payload',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='file',
            name='uploader',
            field=models.CharField(default='----', max_length=100),
            preserve_default=False,
        ),
    ]