# Generated by Django 4.0.3 on 2022-03-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_orderpending_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpending',
            name='totalprice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='orderpending',
            name='totalquantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]