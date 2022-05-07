from random import randint

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection

# Login

def login(request):
    global email
    email = request.GET['email']
    password = request.GET['psw']
    cursor = connection.cursor()
    # to fetch the data from database
    query = "select * from users where email='" + email + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        data = {"message": "Please Register first"}
        return render(request, "verified.html", data)

    if row[3]== password:
        otp=randint(1000,9999)
        value2=(otp,)
        query2="update users set otp=%s where email='" + email + "'"
        cursor.execute(query2,value2)
        data = {"email": row[2], "password": row[3], "mobile_no" :row[4],"date_of_birth": row[8]}
        return render(request, "otp_verification.html", data)
    else:
        data = {"message": "Wrong password !! Please try Again"}
        return render(request, "verified.html", data)


#verification of OTP
def verify(request):
    otp_recived= request.GET['otp']
    cursor = connection.cursor()
    query3 = "select * from users where email='" + email + "'"
    cursor.execute(query3)
    row = cursor.fetchone()
    if otp_recived == row[6] and row[5]==0:
        query3 = "update users set is_verified=%s where email='" + email + "'"
        value3=(1,)
        cursor.execute(query3,value3)
        data={ "message":"YOU ARE VIERIFIED!"}
        return render(request, "verified.html",data)
    elif otp_recived == row[6] and row[5]=="1":
        return render(request, "reset password.html")
    else:
        data={ "message":"YOU ARE not VIERIFIED!! please enter correct otp"}
        return render(request, "verified.html",data)