# Generated by Django 3.1.1 on 2020-10-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0025_auto_20201024_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredient',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(default=''),
        ),
    ]