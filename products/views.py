from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def product_list(request):
    productlist = Product.objects.all().order_by('-created')

    paginator = Paginator(productlist, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    return render(request, "product-list.html", {'productlist': productlist})
