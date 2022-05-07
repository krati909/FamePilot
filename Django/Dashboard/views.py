from random import randint
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection

#Display of data

def dashboard(request):
    global email
    email = request.GET['email']
    password = request.GET['psw']
    cursor = connection.cursor()
    # to fetch the data from database
    query = "select * from users where email='" + email + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    data = {"name":row[1],"email": row[2], "password": row[3], "mobile_no" :row[4],"date_of_birth": row[8]}
    return render(request, "Dashboard.html", data)

