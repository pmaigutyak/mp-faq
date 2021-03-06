# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-25 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('order',), 'verbose_name': 'Frequent asked question', 'verbose_name_plural': 'Frequently asked questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        )
    ]
