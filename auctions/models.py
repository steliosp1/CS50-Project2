from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=60)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(null=True, max_length=300)
    startingBid = models.FloatField()
    currentBid = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="similar_listings")
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    picture = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.jpg')
    active = models.CharField(default='TRUE',max_length=5)
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_listings")
    finalBuyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name="finalBuyer")

    def __str__(self):
        return f"{self.title} | {self.category}"

class Bid(models.Model):
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.FloatField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.auction} | {self.user} | {self.offer}"

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_comments")

    def __str__(self):
        return f"{self.listing} | {self.user}"
