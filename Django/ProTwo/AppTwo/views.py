from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   #t=Template('<html><body><em>My second app jjj</em></body></html>')
   #t=Template('<em>My second app</em>')
   #return HttpResponse(t)
   return render(request,'index.html')

def help(request):
    return render(request,'Help_Page.html')
