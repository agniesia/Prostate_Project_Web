# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0003_auto_20141119_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaProjectContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=30)),
                ('about', models.TextField()),
                ('data_base_description', models.TextField()),
                ('data_base_page_content', models.TextField()),
                ('publications_description', models.TextField()),
                ('publications_page_content', models.TextField()),
                ('contact_description', models.TextField()),
                ('contact_description_page_content', models.TextField()),
                ('contact_address', models.TextField()),
                ('contact_phone', models.CharField(max_length=12)),
                ('contact_email', models.EmailField(max_length=75)),
                ('footer', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
