# Generated by Django 2.2.3 on 2019-08-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190822_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardu',
            name='text',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
