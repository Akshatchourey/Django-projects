# Generated by Django 4.0.5 on 2023-06-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plcomment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneNo',
            field=models.PositiveIntegerField(),
        ),
    ]
