# Generated by Django 4.0.3 on 2022-03-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alluser'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('imageurl', models.CharField(blank=True, max_length=500, null=True)),
                ('imagefilename', models.CharField(blank=True, max_length=500, null=True)),
                ('instock', models.BooleanField(default=True)),
                ('unit', models.CharField(default='-', max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
        ),
    ]