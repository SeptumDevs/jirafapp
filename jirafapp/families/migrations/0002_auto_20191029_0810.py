# Generated by Django 2.2.6 on 2019-10-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='username',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]
