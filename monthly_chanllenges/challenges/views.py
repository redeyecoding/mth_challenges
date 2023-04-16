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

def monthly_challenge_by_numbers(request, jeff_month_by_number):
    match jeff_month_by_number:
        case 1:
            return HttpResponse("Its january but in number format.")
        case 2:
            return HttpResponse("Its february but in number format.")
        case 3:
            return HttpResponse("Its march but in number format.")
        case 4:
            return HttpResponse("Its april but in number format.")
        case 5:
            return HttpResponse("Its may but in number format.")
        case 6:
            return HttpResponse("Its june but in number format.")
        case _:
            return HttpResponseNotFound("This Month is Not Supported")
        
    return HttpResponseNotFound("nope")

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