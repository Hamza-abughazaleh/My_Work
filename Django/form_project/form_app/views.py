from django.shortcuts import render
from . import forms
from form_app.models import form_submit
# Create your views here.

def index(request):
    return render(request,'form_app/home.html')

def form_view(request):
    #if request.method == 'POST':
    #    name = request.POST['name']
    #    email = request.POST['email']
    #    text = request.POST['text']
    #    print(name)
    #    print(email)
    #    print(text)
    form = forms.Form_Name()
    if request.method == 'POST':
        form = forms.Form_Name(request.POST)

        if form.is_valid():
            form_user_information = form_submit.objects.get_or_create(name=form.cleaned_data['name'],
                                                     email=form.cleaned_data['email'],
                                                     text=form.cleaned_data['text'])[0]
            #print("VALIDATIONSUCCESS !")
            #print("NAME :"+form.cleaned_data['name'])
            #print("EMAIL :"+form.cleaned_data['email'])
            #print("TEXT :"+form.cleaned_data['text'])
    return render(request,'form_app/form.html',{'form':form})
