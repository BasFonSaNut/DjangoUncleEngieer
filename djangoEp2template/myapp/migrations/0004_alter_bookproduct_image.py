# Generated by Django 4.0.3 on 2022-03-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_orderpending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookproduct',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='books/'),
        ),
    ]