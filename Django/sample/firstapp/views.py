from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
'''def display(request):
    return HttpResponse("<h1> Hello world </h1>")'''
def display1(request):
    return HttpResponse("<h1> Display1 </h1>")
def welcome(request):
    return render(request,'test.html')
def display(request):
    date = datetime.datetime.now()
    msg = "date test"
    t = {'date':date,'str':msg}
    return render(request,'test.html',context = t)
def add(request):
    return render(request,'add.html')
def add2(request):
    v1 = request.GET["n1"]
    v2 = request.GET["n2"]
    res = int(v1)+int(v2)
    return render(request,'add2.html',{'result':res})
