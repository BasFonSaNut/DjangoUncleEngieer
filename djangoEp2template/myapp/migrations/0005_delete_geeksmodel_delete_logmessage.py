# Generated by Django 4.0.3 on 2022-03-09 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_bookproduct_image_alter_profile_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeeksModel',
        ),
        migrations.DeleteModel(
            name='LogMessage',
        ),
    ]