# Generated by Django 2.2.5 on 2019-11-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20191115_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('amharic', 'AMHARIC')], max_length=10),
        ),
    ]