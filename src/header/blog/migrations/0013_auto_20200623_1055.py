# Generated by Django 3.0.7 on 2020-06-23 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_group_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Groups',
        ),
    ]
