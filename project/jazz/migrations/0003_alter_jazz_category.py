# Generated by Django 4.2.2 on 2023-06-21 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('jazz', '0002_jazz_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jazz',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorys'),
        ),
    ]
