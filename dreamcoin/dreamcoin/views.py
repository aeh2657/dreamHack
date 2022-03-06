from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.template.loader import get_template
   
def home_page(request):
    return render(request, "Home.html")

def about_page(request):
    return HttpResponse('<h1> About Dream Coin </h1>')

def contact_page(request):
    return HttpResponse('<h1> Contact Dream Coin </h1>')

