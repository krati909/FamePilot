from random import randint

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection


def forget(request):
    global email
    email = request.GET['email']
    otp = randint(1000, 9999)
    strotp = str(otp)
    cursor = connection.cursor()
    query = "update users set otp=%s where email='" + email + "'"
    value = (strotp,)
    cursor.execute(query, value)
    # sending a mail
    body = "Your opt for our portal signup with mail " + email + "is" + strotp + "."
    send_mail('OTP for verification', body, "nightullu220@gmail.com", [email])
    return render(request, " otp_verification.html")

def reset(request):
    email = request.GET['email']
    password = request.GET['psw']
    cursor = connection.cursor()
    value2 =(password,)
    query2 = "update users set password=%s where email='" + email + "'"
    cursor.execute(query2, value2)
    data = {"message": "PASSWORD UPDATED SUCESSFULLY"}
    return render(request, "verified.html", data)