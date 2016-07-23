# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BbsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.CharField(default=b'The guy leave nothing', max_length=128)),
                ('icon', models.ImageField(default=b'upload_imgs/user-1.jpg', upload_to=b'upload_imgs/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bbs_user',
            name='user',
        ),
        migrations.AlterField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app.BbsUser'),
        ),
        migrations.DeleteModel(
            name='Bbs_user',
        ),
    ]
