from django.urls import path
from . import views

# if a request comes into challenges/january then execute the jeff_index function.
urlpatterns = [
    path("<int:jeff_month_by_number>", views.monthly_challenge_by_numbers),
    path("<str:jeff_month>", views.monthly_challenge, name="months_text_format")
]