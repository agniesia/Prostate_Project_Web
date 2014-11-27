# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_info', '0013_auto_20141127_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=40)),
                ('contact_email', models.EmailField(max_length=75)),
                ('telephone_number', models.DecimalField(max_digits=15, decimal_places=0)),
                ('address', models.CharField(max_length=200)),
                ('project_email', models.EmailField(max_length=75)),
                ('institutions', models.TextField()),
                ('map', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
