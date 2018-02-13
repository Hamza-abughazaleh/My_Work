from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage

# Create your views here.
def index(request):
   webpages_list = AccessRecord.objects.order_by('date')
   date_dict = {'access_records':webpages_list}
   #vas={'insert_me':"hahahahahaahahah"}
   return render(request,'index.html',context=date_dict)
