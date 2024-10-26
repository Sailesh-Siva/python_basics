from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student
from .forms import Student_form

# Create your views here.
def display(request):
    form = Student.objects.all()
    return render(request,"display.html",context={"form": form})

def insert_view(request):
    form = Student_form()
    if request.method == "POST":
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/display/")
    return render(request,'insert.html',context={'form':form})

def update_view(request,t):
    student = Student.objects.get(sid=t)
    form = Student_form(instance = student)
    if request.method == "POST":
        form = Student_form(request.POST,instance = student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/display/')
    return render(request,"update.html",context={"student" : form})
    
def delete_view(request,t):
    student = Student.objects.get(sid=t)
    student.delete()
    return HttpResponseRedirect('/display/')

