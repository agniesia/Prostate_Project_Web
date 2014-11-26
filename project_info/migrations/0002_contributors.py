# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15)),
                ('names', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
