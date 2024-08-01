from django.urls import path
from .views import main


# link the url to the views
urlpatterns = [
    path('home', main)
]
