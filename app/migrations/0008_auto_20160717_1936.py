# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160715_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='bbs',
            old_name='ranking',
            new_name='like_count',
        ),
        migrations.RemoveField(
            model_name='category',
            name='create_time',
        ),
    ]
