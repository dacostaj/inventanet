# Generated by Django 2.0.1 on 2018-04-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0005_auto_20180430_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='price_c',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='stock',
            field=models.IntegerField(),
        ),
    ]