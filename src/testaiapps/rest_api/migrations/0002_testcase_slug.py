# Generated by Django 3.2.4 on 2021-06-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='slug',
            field=models.SlugField(default='first'),
            preserve_default=False,
        ),
    ]
