# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0009_auto_20141127_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='title',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
