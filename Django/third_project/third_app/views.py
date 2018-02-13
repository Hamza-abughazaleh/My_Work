from django.shortcuts import render
#from third_app.models import Users
from third_app.forms import NewUserForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def user(request):
    #user=Users.objects.all()
    #date_dict = {'access_records':user}
    #return render(request,"user.html",context=date_dict)

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'user.html',{'form':form})
