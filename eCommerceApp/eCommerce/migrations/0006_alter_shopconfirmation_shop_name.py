# Generated by Django 5.0.6 on 2024-06-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0005_alter_shopconfirmation_shop_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopconfirmation',
            name='shop_name',
            field=models.CharField(max_length=50),
        ),
    ]