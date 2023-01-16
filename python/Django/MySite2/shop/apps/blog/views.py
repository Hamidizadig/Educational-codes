from django.shortcuts import render
from django import HttpResponse

# Create your views here.
def showBlogList(request):
    return HttpResponse('list M')