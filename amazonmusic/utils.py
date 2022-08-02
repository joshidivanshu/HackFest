from django.core import send_mail
from django.http import HttpResponse


def sendEmailNotification(emailTo, artistName):
    response = send_mail("Hi , A new songs has been added to"+str(artistName))
    return "Email sent successfully!!"