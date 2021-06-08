from django.shortcuts import render
from .models import Computers 


def products(request):

    products = Computers.objects.all()

    context = {
        #'products' : products.order_by('price')
        #'products' : products.exclude(price=950)
        'products' : products.filter(price__range=[1000,100000])
    }

    return render(request,'products/products.html',context)


def product(request):


    context = {}
    return render(request,'products/product.html')

