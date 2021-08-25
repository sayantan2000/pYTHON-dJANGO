from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(request):
  return render(request, 'shop/About.html')

def trackOrder(request):
    return HttpResponse("Track Your Order")

def contactsUS(request):
    return HttpResponse("Contact Us")

def Complain(request):
    return HttpResponse("Complain Helpline")

