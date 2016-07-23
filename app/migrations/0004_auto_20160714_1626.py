# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160714_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='category',
            field=models.CharField(max_length=16),
        ),
    ]
