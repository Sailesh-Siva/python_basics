from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def add(request):
    v1 = request.GET["n1"]
    v2 = request.GET["n2"]
    res = int(v1) + int(v2)
    return render(request,"result.html",{'result':res})
