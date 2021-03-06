# Generated by Django 2.0.6 on 2018-06-13 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Департамент', 'verbose_name_plural': 'Департаменты'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(default=' ', verbose_name='Описание отдела'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='HomeworkDjango.Shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='department',
            name='sphere',
            field=models.CharField(max_length=250, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='department',
            name='staff_amount',
            field=models.IntegerField(verbose_name='Количество персонала'),
        ),
        migrations.AlterField(
            model_name='item',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='HomeworkDjango.Department', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя товара'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=250, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='staff_amount',
            field=models.IntegerField(verbose_name='Количество персонала'),
        ),
    ]
