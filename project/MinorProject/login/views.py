from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'login/index.html')
def newuser(request):
    return render(request, 'login/new_user.html')
