# Generated by Django 4.2.3 on 2023-09-08 20:04

import apps.utils.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('excerpt', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('cover', models.ImageField(upload_to=apps.utils.files.upload_to)),
                ('cover_content', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=None, max_length=255, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
