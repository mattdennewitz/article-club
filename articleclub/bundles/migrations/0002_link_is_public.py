# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bundles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
