from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def wish(request,data):
    return HttpResponse("welcome to indian navy")