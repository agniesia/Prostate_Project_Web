# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0011_contributor_function'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='function',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
