
# from multiprocessing import context
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
# from django.template import loader
def index(request):
    return HttpResponse('main page site')
# def step1(request):
#     template=loader.get_template('mainapp/page1.html')
#     return HttpResponse(template.render())
def step1(request):
    return render(request,'mainapp/page1.html')
def step2(request):
    context={
        'name':'shahix',
        'age':42,
        'n':100
    }
    return render(request,'mainapp/page2.html',context)
def step3(request):
    context={
        'name':'maxis',
        'age':42,
        'n':100
    }
    return render(request,'mainapp/page3.html',context)
import datetime
def step4(request):
    today=datetime.datetime.now
    context={
        'name':'sasha',
        'age':20,
        'n':100,
        'today':today
    }
    return render(request,'mainapp/page4.html',context)
def step5(request):
    today=datetime.datetime.now
    context={
        'name':'sasha',
        'age':20,
        'n':100,
        'today':today,
        "names":['isa','luxi','sanaf','shengo','safer'],
        'range':range(1,21),
        'list1':[]
    }
    return render(request,'mainapp/page5.html',context)
# def step6(request):
#     today=datetime.datetime.now
#     context={
#         'row':50,
#         'col':100
#     }
#     return render(request,'mainapp/page6.html',context)
def step6(request):
    today=datetime.datetime.now
    context={
        'row':range(50),
        'col':range(100)
    }
    return render(request,'mainapp/page6.html',context)
def step7(request):
    context={
        'mytag':"<h1 style='color:green'>sport</h1>",
        'myscript':"alert(hello Script);"
    }
    return render(request,'mainapp/page7.html',context)
def step8(request):
    return render(request,'mainapp/page8.html')
def step9(request):
    today=datetime.now
    list1=['risius','jasfi','furs','ruts']
    context={
        "str1":'amixus pokshes',
        "today":today,
        "list1":list1
    }
    return render(request,'mainapp/page9.html',context)
import os
def step10(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images')
    context={
        'media_url':settings.MEDIA_URL,
        "imageName":'p2.png',
        "imageList":imageList
    }
    return render(request,'mainapp/page10.html',context)
def step11(request):
    return render(request,'mainapp/page11.html')
def step12(request):
    context={
        'media_url':settings.MEDIA_URL,
        "imageName":'p2.png',
        "imageList":imageList

    }
    return render(request,'mainapp/page12.html',context)