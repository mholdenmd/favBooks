from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.Ribs),
    path("books", views.newsFeed),
    path('approved', views.login),
    path('logout', views.logout),
    path('addNewBook', views.newBook),
    path("books/<int:bookId>", views.bookinfo),
    path("books/<int:bookId>/liked", views.liked)
]