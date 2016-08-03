# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to=b'')),
                ('alt_text', models.CharField(max_length=40)),
                ('caption', models.CharField(max_length=140)),
            ],
        ),
    ]
