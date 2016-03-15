# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160302_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'Blog Image', blank=True),
        ),
    ]
