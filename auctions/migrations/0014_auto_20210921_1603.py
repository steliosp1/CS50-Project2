# Generated by Django 3.2.6 on 2021-09-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_listing_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.CharField(default='TRUE', max_length=5),
        ),
        migrations.AlterField(
            model_name='listing',
            name='picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/'),
        ),
    ]
