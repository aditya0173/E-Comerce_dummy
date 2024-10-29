# Generated by Django 5.0.7 on 2024-10-26 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_accounts_cart_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('shipping_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.carts')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.accounts')),
            ],
        ),
    ]