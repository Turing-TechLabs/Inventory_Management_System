# Generated by Django 3.2.4 on 2023-06-30 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0026_alter_inventory_total_bal_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_mobile',
            field=models.CharField(default='0', max_length=50),
        ),
    ]