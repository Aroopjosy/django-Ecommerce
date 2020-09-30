# Generated by Django 3.0.8 on 2020-08-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-img/')),
                ('available', models.CharField(blank=True, choices=[('OUT', 'Out of Stok'), ('IN', 'In Stock')], max_length=3, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
