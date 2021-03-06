# Generated by Django 2.0.6 on 2018-06-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkDjango', '0003_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='creation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='item',
            name='is_sold',
            field=models.BooleanField(default=False, verbose_name='Продан'),
        ),
    ]
