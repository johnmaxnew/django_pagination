from django.shortcuts import render
from .models import Product

# Create your views here.


def product_list(request):
    productlist = Product.objects.all().order_by('-published')

    return render(request, "product-list.html", {'productlist': productlist})
