# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field=750, null=True, upload_to='images/', width_field=420),
        ),
    ]