# Generated by Django 5.1.1 on 2024-09-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_product', models.IntegerField(primary_key=True, serialize=False)),
                ('name_prod', models.CharField(blank=True, max_length=50)),
                ('price_prod', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('stock_prod', models.IntegerField(blank=True)),
            ],
        ),
    ]
