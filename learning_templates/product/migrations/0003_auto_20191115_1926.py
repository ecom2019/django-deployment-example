# Generated by Django 2.2.5 on 2019-11-15 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191115_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadlinks',
            name='download',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_download_link', to='product.Product'),
        ),
    ]
