from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def january(request):
#     #this will send whatever we configure here to the browser when we get a request.
#     return HttpResponse("This Django project works!")

# def february(request):
#     return HttpResponse("Its february ...Trade the Markets ( Futures )")


# def march(request):
#     return HttpResponse("March contract trading")

# def april(request):
#     return HttpResponse("April: trade some more.")

# def may(request):
#     return HttpResponse("Its May..may showers")

def monthly_challenge(request, jeff_month):
    match jeff_month:
        case 'january':
            return HttpResponse("Its january")
        case 'february':
            return HttpResponse("Its february")
        case 'march':
            return HttpResponse("Its march")
        case 'april':
            return HttpResponse("Its april")
        case 'may':
            return HttpResponse("Its may")
        case 'june':
            return HttpResponse("Its june")
        case _:
            return HttpResponseNotFound("This Month is Not Supported")

    return HttpResponseNotFound("Contact Support")