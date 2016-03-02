# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='default', unique=True, max_length=140),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
