# Generated by Django 2.2.3 on 2019-08-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cardu_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardu',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]