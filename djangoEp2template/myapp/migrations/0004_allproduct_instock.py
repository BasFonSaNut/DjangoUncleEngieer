# Generated by Django 4.0.2 on 2022-02-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_allproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='instock',
            field=models.BooleanField(default=True),
        ),
    ]