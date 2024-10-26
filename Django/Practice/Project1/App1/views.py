from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
count=0
val = -1
flag = 0
def display1(request):
    return HttpResponse("<h1> Hello world </h1>")

def display2(request):
    return HttpResponse("<h1> Hello world 2</h1>")

def home(request):
    return render(request,"home.html")

def getStudentCount(request):
    global val
    global flag
    val = int(request.GET["no"])
    return render(request,"StudentDetails.html")

def studentDetails(request):
    global val
    global count
    global flag
    count+=1
    if count <= val:  
        name = request.GET["name"]
        roll = request.GET["roll"]
        m1 = request.GET["m1"]
        m2 = request.GET["m2"]
        avg = int(m1)+int(m2)
        flag = 1
        return render(request,"StudentDetails.html",{'flag':flag,'name':name,'roll':roll,'m1':m1,'m2':m2,'average':avg})
    else:
        flag = 2
        return render(request,"StudentDetails.html",{'flag':flag,'msg':"More than " + str(val) + " objects were created"})
        
    
