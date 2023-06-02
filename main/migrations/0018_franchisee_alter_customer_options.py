# Generated by Django 4.0.3 on 2023-05-20 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_customer_remove_sale_customer_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Franchisee',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.customer')),
                ('storeowner', models.CharField(max_length=255)),
                ('storename', models.CharField(max_length=255)),
                ('storeaddress', models.CharField(max_length=255)),
                ('storephone', models.CharField(max_length=255)),
                ('storeemail', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '7. Customers'},
        ),
    ]