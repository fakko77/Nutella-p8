# Generated by Django 3.1.1 on 2020-10-09 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='search.category'),
        ),
    ]
