from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def function1(request):
    m = '<h1>function1</h1>'
    return HttpResponse(m)

