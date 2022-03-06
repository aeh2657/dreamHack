from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
   
def home_page(request):
    return render(request, "hello_world.html")

def about_page(request):
    return HttpResponse('<h1> About Dream Coin </h1>')

def contact_page(request):
    return HttpResponse('<h1> Contact Dream Coin </h1>')

