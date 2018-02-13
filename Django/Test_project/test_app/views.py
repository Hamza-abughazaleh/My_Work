from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    vas={'insert_here':"hahahahahaahahah"}
    return render(request,'index.html',context=vas)

def help(request):
    vas={'insert_here':"This is help Page"}
    return render(request,'help.html',context=vas)
