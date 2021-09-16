from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'Billing/index.html')
def signup(request):
    return render(request, 'Billing/signup.html')

def handlesignup(request):
      return redirect('Billing/home')