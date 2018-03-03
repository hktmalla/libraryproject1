# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0007_auto_20180301_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_title',
            field=models.CharField(choices=[('It', 'IT Department'), ('Computer', 'Computer Department'), ('Bba', ' BBA Department'), ('Electronic', 'Electronic and Communication Department'), ('Civil', 'Civil Department')], max_length=30),
        ),
    ]