# Generated by Django 2.2.6 on 2019-10-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191028_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='slug_name',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]
