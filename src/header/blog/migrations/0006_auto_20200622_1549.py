# Generated by Django 3.0.7 on 2020-06-22 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserProfile', verbose_name="O'qituvchi"),
        ),
    ]
