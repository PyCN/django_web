# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_category_c_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['create_time']},
        ),
        migrations.RemoveField(
            model_name='category',
            name='c_id',
        ),
        migrations.AddField(
            model_name='category',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 1, 59, 8, 85000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
