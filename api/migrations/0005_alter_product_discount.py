# Generated by Django 4.2.7 on 2023-11-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_discount_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=''),
            preserve_default=False,
        ),
    ]
