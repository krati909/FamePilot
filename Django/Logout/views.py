from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def logout(request):
    return render(request, "login.html")