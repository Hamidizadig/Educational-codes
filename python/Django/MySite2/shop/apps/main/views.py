from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Your wellcomme')

def step1(request):
    return HttpResponse('Step1')

def step2(request):
    return HttpResponse('sddddddddddddddddddd')

def page1(request):
    
    return HttpResponse()
    