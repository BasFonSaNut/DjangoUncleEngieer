# Generated by Django 4.0.2 on 2022-02-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_geeksmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]