# Generated by Django 4.2.5 on 2024-05-19 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0015_purchaseorder_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='restockedproduct',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.supplier'),
        ),
    ]
