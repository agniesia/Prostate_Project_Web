# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0012_auto_20141127_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='function',
            field=models.CharField(default=1, max_length=30, blank=True),
            preserve_default=False,
        ),
    ]
