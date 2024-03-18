from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':1})
    # print(request)
    # return HttpResponse("Hello World")


def add(request):
    num1 = request.POST["num1"]
    num2 = request.POST["num2"]
    val = int(num1) + int(num2)
    # print(num1)
    # print(type(num1))
    return render(request,'result.html',{'result': val})



def get_add(request):
    num1 = request.GET["num3"]
    num2 = request.GET["num4"]
    val = int(num1) + int(num2)
    # print(num1)
    # print(type(num1))
    return render(request,'result.html',{'result': val})