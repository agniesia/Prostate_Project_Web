# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('project_info', '0005_delete_metaprojectcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('ole', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=('flatpages.flatpage',),
        ),
    ]
