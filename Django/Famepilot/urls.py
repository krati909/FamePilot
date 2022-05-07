"""Famepilot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Application.view import start, register, resetpassword
from Login.views import login, verify
from Logout.views import logout
from Register.views import signup
from Reset.views import forget, reset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', start),
    path('register/', register),
    path('resetpassword/', resetpassword),
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout),
    path('verify/', verify),
    path('forget/', forget),
    path('reset/', reset),
    path('Application/',include('Applications.urls'))

]
