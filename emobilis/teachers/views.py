from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (request):
    return HttpResponse ("about emobilis")

def menu (reguest):
    return HttpResponse ("Menu")