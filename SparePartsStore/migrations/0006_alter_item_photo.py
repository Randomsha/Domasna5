# Generated by Django 4.2.2 on 2023-06-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SparePartsStore', '0005_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images'),
        ),
    ]
