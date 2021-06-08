from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.products,name="products"),
    path('product',views.product,name="product"),
]