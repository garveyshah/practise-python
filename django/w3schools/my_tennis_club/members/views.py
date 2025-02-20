from django.shortcuts import render
from django.http import HttpResponse

def myworld(request):
    return HttpResponse("This is my World !")



def members(request):
    return HttpResponse("Hello world!")

