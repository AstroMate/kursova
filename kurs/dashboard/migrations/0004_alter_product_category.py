# Generated by Django 4.2.7 on 2023-11-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_order_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Верхній одяг', 'Верхній одяг'), ('Взуття', 'Взуття'), ('Штани', 'Штани'), ('Куртка', 'Куртка'), ('Головний убір', 'Головний убір')], max_length=50, null=True),
        ),
    ]