from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="shophome"),
    path("about/",views.about,name="aboutus"),
    path("contact/",views.contact1,name="contactus"),
    path("tracker/",views.tracker,name="trackingstatus"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>", views.products, name="products"),
    path("checkout/",views.checkout,name="checkout"),
    # path("handlerequest/",views.handlerequest,name="HandleRequest"),
]