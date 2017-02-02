# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170202_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
    ]
