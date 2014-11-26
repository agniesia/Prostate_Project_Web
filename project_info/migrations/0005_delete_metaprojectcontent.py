# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0004_metaprojectcontent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MetaProjectContent',
        ),
    ]
