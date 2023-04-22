from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

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

# def monthly_challenge_by_numbers(request, jeff_month_by_number):
#     match jeff_month_by_number:
#         case 1:
#             return HttpResponse("Its january but in number format.")
#         case 2:
#             return HttpResponse("Its february but in number format.")
#         case 3:
#             return HttpResponse("Its march but in number format.")
#         case 4:
#             return HttpResponse("Its april but in number format.")
#         case 5:
#             return HttpResponse("Its may but in number format.")
#         case 6:
#             return HttpResponse("Its june but in number format.")
#         case _:
#             return HttpResponseNotFound("This Month is Not Supported")
        
#     return HttpResponseNotFound("nope")

# def monthly_challenge(request, jeff_month):
#     match jeff_month:
#         case 'january':
#             return HttpResponse("Its january")
#         case 'february':
#             return HttpResponse("Its february")
#         case 'march':
#             return HttpResponse("Its march")
#         case 'april':
#             return HttpResponse("Its april")
#         case 'may':
#             return HttpResponse("Its may")
#         case 'june':
#             return HttpResponse("Its june")
#         case _:
#             return HttpResponseNotFound("This Month is Not Supported")

#     return HttpResponseNotFound("Contact Support")

monthly_challenges = {
    "january": "Its jan",
    "feb": "Its feb",
    "mar": "Its mar",
    "apr": "Its apr",
    "may": "Its may",
    "jun": "Its un",
    "july": "Its july",
    "aug": "Its aug",
    "sept": "Its sept",
}

monthly_challenges_via_number = {
    1: "Its jan via number",
    2: "Its feb via number",
    3: "Its mar via number",
    4: "Its apr via number",
    5: "Its may via number",
    6: "Its un via number",
    7: "Its july via number",
    8: "Its aug via number",
    9: "Its sept via number",
}



def monthly_challenge(request, jeff_month):
    try:
        challenge_text = monthly_challenges[jeff_month]
        return render(request, "challenges/challenge.html", {
            "jeff_text": challenge_text,
            "month_key": jeff_month
        })
    except:
        return HttpResponseNotFound("<h1> This month is not supported</h1>")
    return HttpResponse(reponse_html_data)



def monthly_challenge_by_numbers(request, jeff_month_by_number):
    #Redirect the number of a month to its string value.
    month = list(monthly_challenges.keys())

    if jeff_month_by_number > len(month): 
        return HttpResponseNotFound("invalid MONTH")

    response_redirect_month = month[jeff_month_by_number - 1]
    redirect_path = reverse("months_text_format", args=[response_redirect_month])  # creates path "challenges/january"
    return HttpResponseRedirect(redirect_path)


def index(request):
    list_of_months = list(monthly_challenges.keys())
 
    return render(request, "challenges/index.html", {
        "list_of_mths": list_of_months
    })


