from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    #this will send whatever we configure here to the browser when we get a request.
    return HttpResponse("This Django project works!")

def february(request):
    return HttpResponse("Its february ...Trade the Markets ( Futures )")


def march(request):
    return HttpResponse("March contract trading")

def april(request):
    return HttpResponse("April: trade some more.")

def may(request):
    return HttpResponse("Its May..may showers")

