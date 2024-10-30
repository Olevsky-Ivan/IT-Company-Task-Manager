# Generated by Django 5.1.2 on 2024-10-28 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignees',
            field=models.ManyToManyField(blank=True, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='task_manager.tag'),
        ),
    ]