# Generated by Django 4.0.4 on 2022-05-11 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proid', models.IntegerField()),
                ('proname', models.CharField(max_length=70)),
                ('prodisc', models.CharField(max_length=200)),
                ('protype', models.CharField(max_length=70)),
            ],
        ),
    ]