# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160714_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='c_id',
            field=models.IntegerField(default=datetime.datetime(2016, 7, 15, 1, 32, 46, 739000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
