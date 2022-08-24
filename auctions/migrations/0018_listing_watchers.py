# Generated by Django 3.2.6 on 2021-09-23 20:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watched_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
