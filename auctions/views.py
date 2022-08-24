from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import *
from .forms import newListingForm
from django.contrib import messages #import messages
from django.shortcuts import get_object_or_404

from .models import User


def index(request):
    all_listings = Listing.objects.filter(active='TRUE')
    return render(request, "auctions/index.html", {
        'all':all_listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url="login")
def new_listing(request):
    lastimage = Listing.objects.last()
    picture=lastimage.picture
    form = newListingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        myForm = form.save()
        myForm.user = request.user
        myForm.save()
        messages.success(request, 'Listing has been submitted successfully.')
    context = {'form':form}
    return render(request, 'auctions/newListing.html', context)

def detail(request,pk):
    products = Listing.objects.get(id=pk)

    post = get_object_or_404(Listing, id=pk)
    fav = bool

    if post.watchers.filter(id=request.user.id).exists():
        fav = True

    context = {'products':products,'fav':fav}
    return render(request,"auctions/certainListing.html", context)

def category(request):
    categories = Category.objects.all
    context = {'categories':categories}
    return render(request, "auctions/categories.html", context)

def certainCategory(request):
    item = request.GET.get('item')

    if item == None:
        all_listings = Listing.objects.filter(active='TRUE')
    else:
        all_listings = Listing.objects.filter(category__category=item).filter(active='TRUE')

    context = {'all_listings':all_listings, 'item':item}
    return render(request, "auctions/certainCategories.html", context)

@login_required(login_url="login")
def favourite_add(request,id):
    post = get_object_or_404(Listing, id=id)
    if post.watchers.filter(id=request.user.id).exists():
        post.watchers.remove(request.user)
        messages.error(request, 'Item removed from watchlist.')
    else:
        messages.success(request, 'Item added to watchlist.')
        post.watchers.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def favourite_list(request):
    new = Listing.objects.filter(watchers=request.user)
    return render(request, 'auctions/watchlist.html',{'new':new})


@login_required(login_url="login")
def take_bid(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    post = get_object_or_404(Listing, id=listing_id)
    fav = bool

    if post.watchers.filter(id=request.user.id).exists():
        fav = True
    if request.method == "POST":
        offer = float(request.POST["offer"])
        if is_valid(offer, listing):
            listing.currentBid = offer
            form = newBidForm(request.POST)
            if form.is_valid():
                newBid = form.save(commit=False)
                newBid.auction = listing
                newBid.user = request.user
                newBid.save()
                listing.save()
                messages.success(request, 'Bid accepted !')
            return render(request, 'auctions/certainListing.html', {'products':listing,'fav':fav})
        else:
            return render(request, "auctions/certainListing.html", {
                "products": listing,
                "form": newBidForm(),
                "error_min_value": True
            })

def is_valid(offer, listing):
    if offer >= listing.startingBid and (listing.currentBid is None or offer > listing.currentBid):
        return True
    else:
        return False

@login_required(login_url="login")
def createComment(request, pk):
    listing = Listing.objects.get(id=pk)

    post = get_object_or_404(Listing, id=pk)
    fav = bool

    if post.watchers.filter(id=request.user.id).exists():
        fav = True
    if request.method == "POST":
        comments = request.POST["comments"]
        form = Comment(comment = comments, user = request.user, listing = listing)
        form.save()

    context = {'products':listing,'fav':fav}
    return render(request, 'auctions/certainListing.html', context)

def close_listing(request,listing_id):
    listing = Listing.objects.get(id=listing_id)

    post = get_object_or_404(Listing, id=listing_id)
    fav = bool

    if post.watchers.filter(id=request.user.id).exists():
        fav = True

    if request.user == listing.user:
        listing.active = False
        listing.finalBuyer = Bid.objects.filter(auction=listing).last().user
        listing.save()
        context = {'products':listing,'fav':fav}
        return render(request, 'auctions/certainListing.html', context)
    else:
        listing.watchers.add(request.user)
        return HttpResponseRedirect(reverse("watchlist"))
