# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160717_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bbs',
            old_name='like_count',
            new_name='ranking',
        ),
    ]
