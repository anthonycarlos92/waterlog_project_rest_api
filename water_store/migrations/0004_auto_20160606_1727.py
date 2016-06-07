# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0003_auto_20160606_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservoir',
            name='inflow',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='outflow',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='precipitation_accumulated',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='precipitation_incremental',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='storage_capacity',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
    ]