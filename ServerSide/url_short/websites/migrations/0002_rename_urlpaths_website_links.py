# Generated by Django 4.1.3 on 2022-11-29 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='URLpaths',
            new_name='website_links',
        ),
    ]
