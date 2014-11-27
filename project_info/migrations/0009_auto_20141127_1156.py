# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0008_publicationflatpage_ole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationflatpage',
            name='flatpage_ptr',
        ),
        migrations.RemoveField(
            model_name='publicationflatpage',
            name='ole',
        ),
        migrations.DeleteModel(
            name='PublicationFlatPage',
        ),
    ]
