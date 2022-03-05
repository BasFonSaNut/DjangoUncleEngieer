# Generated by Django 4.0.2 on 2022-02-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_logmessage_log_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('imageurl', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
