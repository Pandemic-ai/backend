# Generated by Django 2.2 on 2020-03-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_auto_20200321_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportpeople',
            name='date',
            field=models.DateField(null=True, verbose_name='Date of register'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='date',
            field=models.DateField(null=True, verbose_name='Date of register'),
        ),
    ]
