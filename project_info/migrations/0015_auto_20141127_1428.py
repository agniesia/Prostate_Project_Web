# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0014_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telephone_number',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
