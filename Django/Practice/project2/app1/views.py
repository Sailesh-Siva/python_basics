from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Employee,Product
from .forms import Employee_form,Product_form
# Create your views here.

def home(request):
    return render(request,"home.html")

def option(request):
    choice = request.GET["choice"]
    if(choice == "E"):
        return render(request,"EmployeeMenu.html")
    elif(choice =="P"):
        return render(request,"ProductMenu.html")
    return HttpResponse("Testing")

def option2(request):
    choice = request.GET["choice"]
    choice2 = request.GET["choice2"]
    if(choice == "1"):
        return empinsert(request)
    if(choice == "2"):
        return empupdate(request,choice2)
    if(choice == "3"):
        return empdisplay(request)
    if(choice == "4"):
        return empsearch(request,choice2)
    if(choice == "5"):
        return empdelete(request,choice2)

def empinsert(request):
    form = Employee_form()
    if request.method == "POST":
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"EmployeeMenu.html")
    return render(request,'InsertEmployee.html',context={'form':form})

def empdisplay(request):
    form = Employee.objects.all()
    return render(request,'DisplayEmployee.html',context={'form':form})

def empupdate(request,choice2):
    employee = Employee.objects.get(empid = choice2)
    form = Employee_form(instance = employee)
    if request.method == "POST":
        form = Employee_form(request.POST,instance = employee)
        if form.is_valid():
            form.save()
            return render(request,"EmployeeMenu.html")
    return render(request,"UpdateEmployee.html",context={"employee" : form})

def empsearch(request,choice2):
    employee = Employee.objects.get(empid = choice2)
    #form = Employee_form(instance = employee)
    return render(request,"SearchEmployee.html",context={"employee" : employee})

def empdelete(request,choice2):
    employee = Employee.objects.get(empid = choice2)
    employee.delete()
    return empdisplay(request)















            
