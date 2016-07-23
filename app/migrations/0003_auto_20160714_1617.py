# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160711_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='summary',
        ),
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbsuser',
            name='icon',
            field=models.ImageField(default=b'upload_imgs/nicai.jpg', upload_to=b'upload_imgs/'),
        ),
    ]
