from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='color:red';>Hello Djengo</h1>")

def page1(request):
    x=1000
    y=2000
    z=x*y
    
    return HttpResponse("صفحه اول سایت"+str(z))