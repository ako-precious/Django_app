from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
# def home_view(request, *args,**kwargs):
#     return HttpResponse("<h1> Hello world </h1>")


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
        
    }
    return render(request, "product/detail.html", context)