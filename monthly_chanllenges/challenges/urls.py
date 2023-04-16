from django.urls import path
from . import views

# if a request comes into challenges/january then execute the jeff_index function.
urlpatterns = [
    path("<jeff_month>", views.monthly_challenge)
]