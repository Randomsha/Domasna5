# Generated by Django 4.2.2 on 2023-06-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SparePartsStore', '0003_rename_categories_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
