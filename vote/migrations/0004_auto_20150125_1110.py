# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20150125_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='constituency',
            field=models.ForeignKey(to='vote.Constituency', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='response',
            name='party',
            field=models.ForeignKey(to='vote.Party', null=True),
            preserve_default=True,
        ),
    ]
