# Generated by Django 4.2.2 on 2023-06-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jazz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author_Name', models.CharField(max_length=50)),
                ('Author_Sure_Name', models.CharField(max_length=50)),
                ('Author_Age', models.PositiveIntegerField()),
                ('Info', models.TextField()),
            ],
        ),
    ]