# Generated by Django 4.2.3 on 2023-08-15 12:12

import apps.site_setup.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_menulink_site_setup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='fav_icon',
            field=models.ImageField(blank=True, default='', upload_to=apps.site_setup.models.upload_to),
        ),
    ]