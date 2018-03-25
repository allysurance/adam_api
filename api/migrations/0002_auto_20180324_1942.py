# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='lumpsum',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='fbid',
            new_name='maturity_term',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='mobile',
            new_name='premium_afford',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='premium_term',
        ),
        migrations.AddField(
            model_name='user',
            name='sender_id',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='smoking_status',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
    ]
