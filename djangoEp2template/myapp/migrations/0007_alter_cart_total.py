# Generated by Django 4.0.3 on 2022-03-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
