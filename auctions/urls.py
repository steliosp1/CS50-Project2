from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing/", views.new_listing, name="new_listing"),
    path('detail/<int:pk>', views.detail,name="detail"),
    path('category/', views.category, name="category"),
    path('certainCategory/', views.certainCategory, name="certainCategory"),
    path('fav/<int:id>/', views.favourite_add, name="favourite_add"),
    path('favourite_list', views.favourite_list, name="favourite_list"),
    path('take_bid/<int:listing_id>/', views.take_bid, name="take_bid"),
    path('createComment/<int:pk>/', views.createComment, name="createComment"),
    path('close_listing/<int:listing_id>/', views.close_listing, name="close_listing"),
    ]
