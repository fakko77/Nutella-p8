# Generated by Django 3.1.1 on 2020-10-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0015_auto_20201009_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
