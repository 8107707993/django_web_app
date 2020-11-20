from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("hello Tracker")


def search(request):
    return HttpResponse("hello Search")


def prodView(request):
    return HttpResponse("hello Productview")


def checkout(request):
    return HttpResponse("hello Checkout")
