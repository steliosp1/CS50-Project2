# Generated by Django 3.2.6 on 2021-09-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210919_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
