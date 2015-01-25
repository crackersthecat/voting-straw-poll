# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20150125_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='will_you_vote',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
