# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0010_auto_20141127_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='function',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
