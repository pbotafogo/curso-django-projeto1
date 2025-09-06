from django.urls import path

from recipes.views import govbr, home

urlpatterns = [
    path('', home),  # Home
    path('govbr', govbr),
]
