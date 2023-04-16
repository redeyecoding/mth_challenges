from django.urls import path
from . import views

# if a request comes into challenges/january then execute the jeff_index function.
urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
    path("april", views.april),
    path("may", views.may),
]