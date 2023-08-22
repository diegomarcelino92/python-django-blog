# Generated by Django 4.2.3 on 2023-08-22 11:12

import apps.site_setup.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0005_sitesetup_fav_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='fav_icon',
            field=models.ImageField(blank=True, default='', upload_to=apps.site_setup.models.upload_to, validators=[apps.site_setup.models.validate_image]),
        ),
    ]
