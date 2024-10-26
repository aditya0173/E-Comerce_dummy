# Generated by Django 5.0.7 on 2024-10-26 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_stock'),
        ('users', '0005_alter_accounts_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='cart_id',
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Address_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=200)),
                ('colony', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('Cart_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.accounts')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
        ),
    ]