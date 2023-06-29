# Generated by Django 4.2.2 on 2023-06-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SparePartsStore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='categories',
            field=models.ManyToManyField(related_name='items', to='SparePartsStore.category'),
        ),
    ]