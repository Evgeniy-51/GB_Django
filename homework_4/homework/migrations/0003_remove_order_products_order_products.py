# Generated by Django 4.2.5 on 2023-09-12 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_alter_customer_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homework.product'),
            preserve_default=False,
        ),
    ]
