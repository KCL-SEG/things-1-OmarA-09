from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #response = HttpResponse("Welcome to Things")
    return render(request, 'home.html')
