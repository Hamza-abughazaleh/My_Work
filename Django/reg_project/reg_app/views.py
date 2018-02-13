from django.shortcuts import render
from reg_app.forms import UserForm,UserPorfileInfoForm
# Create your views here.
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'reg_app/Home.html')

@login_required
def user_logout(request):
   # Log out the user.
   logout(request)
   # Return to homepage.
   return HttpResponseRedirect(reverse('home'))

def register(request):

    registered=False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserPorfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserPorfileInfoForm()

    return render(request,'reg_app/register.html',
                                {'user_form':user_form,
                                 'profile_form':profile_form,
                                 'registered':registered})



def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'reg_app/login.html', {})
