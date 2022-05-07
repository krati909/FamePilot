from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def signup(request):
    name = request.GET['name']
    email = request.GET['email']
    password = request.GET['psw']
    mobile_no = request.GET['mobile_no']
    dob = request.GET['dob']
    data = {"Name":name, "Email": email, "Password": password, "Mobile_No": mobile_no,"Date_of_birth": dob}
    cursor = connection.cursor()

    try:
    # to insert the data into database
        query = "insert into users(Name,Email,Password,Mobile_No,Date_of_birth) values (%s,%s,%s,%s,%s)"
        value = (name,email, password, mobile_no,dob)
        cursor.execute(query, value)
        return render(request, "otp_verification", data)
    except:
        data = {"message": "Session time Out, please try again"}
        return render(request, "verified.html", data)
