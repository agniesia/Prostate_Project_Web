# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0007_remove_publicationflatpage_ole'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationflatpage',
            name='ole',
            field=models.ForeignKey(default=1, to='project_info.Publication'),
            preserve_default=False,
        ),
    ]
