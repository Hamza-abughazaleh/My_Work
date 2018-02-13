from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from DBapp.models import Trip,AuthUser,Tripcomment,Votes,UserProfile
from django.contrib.auth.models import User
from DBapp.forms import TripForm, StoryForm, UserForm,Tripcommentform,UserProfileForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy # it waits until I delete the trip until it view the url
from django.contrib.auth import authenticate, login, logout
# zay el decorator ta3 el functions based view bas lal classes based view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.core.urlresolvers import reverse
import datetime
from django.shortcuts import render_to_response ,render
from django.template import RequestContext

def get_profile(request):
   if request.user.is_authenticated():
       user = AuthUser.objects.get(id=request.user.id)
       userprofiles = UserProfile.objects.all()
       pro = 0
       profile = None
       for profile in userprofiles:
           if profile.user.pk == user.id:
               pro = profile.profile_id
               profile = profile
               return {'user': request.user,'profile':profile}
       return {'user': request.user}
   else:
       return {}
