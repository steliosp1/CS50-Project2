# Generated by Django 3.2.6 on 2021-09-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210920_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='buyer',
        ),
    ]