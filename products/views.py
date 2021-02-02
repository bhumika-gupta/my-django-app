from django.http import HttpResponse
from django.shortcuts import render
#index is main page of products, different pages like new, or trending
from .models import Product


# / products -> index
# url = Uniform Resource Locator (address)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', # template
                  {'products': products}) # the data


def new(request):
    return HttpResponse("Look at our new products!")




