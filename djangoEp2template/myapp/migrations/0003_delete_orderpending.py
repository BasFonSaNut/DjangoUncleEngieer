# Generated by Django 4.0.3 on 2022-03-18 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_orderpending_slip_orderpending_codprice_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderPending',
        ),
    ]