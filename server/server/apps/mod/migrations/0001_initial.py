# Generated by Django 2.2.10 on 2020-03-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('admin', models.BooleanField(default=False)),
                ('classes', models.ManyToManyField(blank=True, related_name='mods', to='course.Course')),
            ],
        ),
    ]
