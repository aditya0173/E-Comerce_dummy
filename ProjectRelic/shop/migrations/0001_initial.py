# Generated by Django 5.0.7 on 2024-10-30 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='PRODUCT_ID')),
                ('title', models.TextField()),
                ('asin', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=100)),
                ('stars', models.DecimalField(decimal_places=1, max_digits=2)),
                ('reviewsCount', models.IntegerField()),
                ('thumbnailImage', models.TextField()),
                ('breadCrumbs', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=1)),
                ('url', models.TextField(default='n/a')),
            ],
        ),
    ]
