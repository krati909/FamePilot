from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def start(request):
    return render(request, "login.html")
def register(request):
    return render(request, "signup.html")
def resetpassword(request):
    return render(request, "forget.html")