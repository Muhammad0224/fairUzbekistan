# Generated by Django 3.0.7 on 2020-06-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20200629_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='vaqt'),
        ),
    ]
