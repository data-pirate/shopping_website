# Generated by Django 3.0.3 on 2020-03-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200304_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('hot', 'hot'), ('new', 'new'), ('sale', 'sale')], max_length=4, null=True),
        ),
    ]