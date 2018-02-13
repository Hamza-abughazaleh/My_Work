from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello word','number':100}
    return render(request,'basic_app/index.html',context=context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def bacis(request):
    return render(request,'basic_app/basic.html')

def relative(request):
    return render(request,'basic_app/relative.html')