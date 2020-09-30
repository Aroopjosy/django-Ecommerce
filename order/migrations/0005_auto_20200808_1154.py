# Generated by Django 3.0.8 on 2020-08-08 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200806_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Address'),
        ),
    ]
