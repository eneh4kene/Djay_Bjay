from django.shortcuts import render
from django.http import HttpResponse

# the main view
def main(request):
    return HttpResponse("<h1>Hello, Senior Software Developer!")

