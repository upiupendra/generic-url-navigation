from django.shortcuts import render

# Create your views here.

def harry(request):
    return render(request,'harry.html')

def poter(request):
    return render(request,'poter.html')