# Generated by Django 3.2.6 on 2021-09-14 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('flActive', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=300, null=True)),
                ('startingBid', models.FloatField()),
                ('currentBid', models.FloatField(blank=True, null=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_listings', to='auctions.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='all_creators_listings', to=settings.AUTH_USER_MODEL)),
                ('watchers', models.ManyToManyField(blank=True, related_name='watched_listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]