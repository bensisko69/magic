# Generated by Django 2.2.3 on 2019-08-20 20:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_deck_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='user',
        ),
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
