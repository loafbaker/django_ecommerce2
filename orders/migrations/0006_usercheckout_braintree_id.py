# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercheckout',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]