# Generated by Django 4.2.5 on 2024-04-29 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_alter_purchaseorder_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.product'),
        ),
    ]
