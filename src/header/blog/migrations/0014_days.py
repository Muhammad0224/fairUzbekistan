# Generated by Django 3.0.7 on 2020-06-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200623_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Hafta kuni')),
            ],
            options={
                'verbose_name': 'Kun',
                'verbose_name_plural': 'Hafta kunlari',
            },
        ),
    ]