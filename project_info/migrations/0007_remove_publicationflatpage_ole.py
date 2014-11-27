# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0006_publicationflatpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationflatpage',
            name='ole',
        ),
    ]
