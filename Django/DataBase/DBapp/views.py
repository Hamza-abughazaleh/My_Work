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
# Create your views here.

class IndexView(TemplateView):
   template_name = 'DBapp/index.html'

class TripListView(ListView):
   model = Trip

   # define how to grab trips list
   # queryset allows to me to use Django ORM when dealing with generic views
   # to add a custom touch to ORM
   # SQL query on my model that grabs the trip model objects and filter it based on my condition
   # date__lte: grabs date
   # and after __ you write the field condition
   # lte is a condition : less than or equal to
   # date : the dash (-) orders them in descending order, the most recent blog trips comes up front
   def get_queryset(self):
       return Trip.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class TripDetailView(DetailView):
   model = Trip

   def get_context_data(self,**kwargs):
       context = super(TripDetailView, self).get_context_data(**kwargs)
       a = get_object_or_404(Trip,id=self.kwargs['pk'])
       context['comments']= Tripcomment.objects.all()
       context['results']={}
       for x in range(len(context['comments'])):
           if context['comments'][x].trip.id == a.id:
               context['results'][x]=context['comments'][x]
       return context
class CreateTripView(LoginRequiredMixin,CreateView):
   # I don't anyone to be able to access this CreateTripView
   # Mixins attributes
   # Specifies where the login url should be
   login_url = '/login/'
   # redirect field :
   redirect_field_name = 'DBapp/trip_detail.html'
   form_class = TripForm

   model = Trip
   def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        userid = AuthUser.objects.get(id=self.request.user.id)
        form.instance.user = userid
        form.instance.votecount = 0
        return super(CreateTripView,self).form_valid(form)

class AddCommentToTrip(LoginRequiredMixin,CreateView):
    login_url = '/login'
    # redirect field :
    redirect_field_name = 'DBapp/trip_detail.html'
    form_class = Tripcommentform
    model = Tripcomment

    def form_valid(self,form):
        userid = AuthUser.objects.get(id=self.request.user.id)
        form.instance.user = userid
        form.instance.date = timezone.localtime()
        tripid = get_object_or_404(Trip,id=self.kwargs['pk'])
        form.instance.trip = tripid
        if userid.id == tripid.user.id:
            form.instance.approved = True
        else:
            form.instance.approved = False
        return super(AddCommentToTrip,self).form_valid(form)


class TripUpdateView(LoginRequiredMixin,UpdateView):
   login_url = '/login/'
   redirect_field_name = 'DBapp/trip_detail.html'
   form_class = TripForm

   model = Trip

class TripDeleteView(LoginRequiredMixin,DeleteView):
   model = Trip
   success_url = reverse_lazy('trip_list')

class DraftListView(LoginRequiredMixin,ListView):
   login_url = '/login/'
   template_name = 'DBapp/trip_draft_list.html'
   redirect_field_name = 'DBapp/trip_list.html'
   model = Trip

# make sure there is no publication date on it
   #def get_queryset(self):
    #   return Trip.objects.filter(publish_date__isnull=True).order_by('-date')
   def get_context_data(self,**kwargs):
        context = super(DraftListView, self).get_context_data(**kwargs)
        a = AuthUser.objects.get(id=self.request.user.id)
        context['trips']= Trip.objects.all()
        context['results']={}
        for x in range(len(context['trips'])):
            if context['trips'][x].user.id == a.id and context['trips'][x].publish_date == None:
                context['results'][x]=context['trips'][x]
        return context

#############################################
#############################################
@login_required
def trip_publish(request,pk):
   trip = get_object_or_404(Trip,pk=pk)
   trip.publish_date=datetime.date.today()
   trip.save()
   return redirect('trip_draft_list')



@login_required
def comment_approve(request,pk):
   comment = get_object_or_404(Tripcomment,pk=pk)
   comment.approved = True
   comment.save()
   return redirect('trip_detail',pk=comment.trip.pk)

class CommentUpdateView(LoginRequiredMixin,UpdateView):
   login_url = '/login/'
   redirect_field_name = 'DBapp/trip_detail.html'
   form_class = Tripcommentform
   model = Tripcomment


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
   login_url = '/login/'
   template_name = "DBapp/edit_profile.html"
   redirect_field_name = 'DBapp/user_profile.html'
   form_class = UserForm
   #second_form_class = UserProfileForm
   model = User

   #def get_context_data(self, **kwargs):
    #    context = super(ProfileUpdateView, self).get_context_data(**kwargs)
    #    context['active_client'] = True
#        if 'form' not in context:
#            context['form'] = self.form_class(self.request.GET)
#            context['form'].save()
#        if 'form2' not in context:
#            context['form2'] = self.second_form_class(self.request.GET)
#        context['active_client'] = True
#        return context

class ProfileimageUpdateView(LoginRequiredMixin,UpdateView):
   login_url = '/login/'
   #template_name = "DBapp/edit_image_profile.html"
   redirect_field_name = 'DBapp/user_profile.html'
   form_class = UserProfileForm
   model = UserProfile



@login_required
def comment_remove(request,pk):
   comment = get_object_or_404(Tripcomment,pk=pk)
   trip_pk = comment.trip.pk
   comment.delete()
   return redirect('trip_detail',pk=trip_pk)


def register(request):
   registered = False

   if request.method == 'POST':
       user_form = UserForm(data=request.POST)
       profile_form = UserProfileForm(data=request.POST)

       if user_form.is_valid() and profile_form.is_valid():
           user2 = user_form.save()
           user2.set_password(user2.password)
           user2.save()
           x = user_form.instance.id
           profile = profile_form.save(commit=False)
           profile_form.instance.user = AuthUser(x)
           profile.save()
           if 'profile_pic' in request.FILES:
               profile.profile_pic = request.FILES['profile_pic']
           profile.save()
           registered = True
       else:
           print(user_form.errors)
           print(profile_form.errors)

   else:
      user_form = UserForm
      profile_form = UserProfileForm

   return render(request,'registration/register.html',{'user_form':user_form,'profile_form':profile_form
                                                        ,'registered':registered})



def user_login(request):
   if request.method == "POST":
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(username=username,password=password)

       if user:
           if user.is_active:
               login(request,user)
               return HttpResponseRedirect(reverse('trip_list'))
           else:
               return HttpResponse("ACCOUNT IS NOT ACTIVE!")
       else:
           print("Some one is trying to login and failed")
           print("Username: {} and Password: {}".format(username,password))
           return HttpResponse("Invalid login details Supplied!")


   else:

       return render(request,'registration/login.html',{})
#def image(u):
#    if UserProfile.objects.filter(user=u).exists():
#        print("You are Exists")
#        print(u)
#        image = UserProfile()
#        print(image.profile_pic)
    #display_test = me_options.option1_photo
    #return render(request, 'lesson/detail.html', {'lesson': lesson, 'display_test':   display_test})
@login_required
def get_user_profile(request, pk):
   user = get_object_or_404(AuthUser, pk=pk)
   userprofiles = UserProfile.objects.all()
   pro = 0
   profile = None
   for profile in userprofiles:
       if profile.user.pk == user.id:
           pro = profile.profile_id
           profile = profile
           return render(request, 'DBapp/user_profile.html',{'user': request.user,'profile':profile})
   return render(request, 'DBapp/user_profile.html',{'user': request.user})


def votesys(self,pk):
   if Votes.objects.filter(user=AuthUser.objects.get(id=self.user.id),trip=Trip.objects.get(id=pk)).exists():
       return HttpResponse("You already voted to this trip!")
   else:
        vote = Votes()
        a = AuthUser.objects.get(id=self.user.id)
        d = Trip.objects.get(id=pk)
        vote.user = a
        vote.trip = d
        vote.save()
        d.votecount+= 1
        d.save()
   return redirect('trip_detail',pk=d.pk)


#def validate_vote(request):
#    user_vote = request.GET.get('myvote',None)

#    data = {
#        'is_taken': Votes.objects.filter(user=AuthUser.objects.get(id=request.self.user.id),trip=Trip.objects.get(id=pk)).exists()

#    }
#    return JsonResponse(data)


def Update(request,pk):
   if request.method == 'POST':
       a = get_object_or_404(AuthUser,id=request.user.id)
       user_profile = UserProfile.objects.get(user=a)
       user_form = UserForm(data=request.POST, instance = request.user)
       profile_form = UserProfileForm(data=request.POST,instance=user_profile)

       if user_form.is_valid() and profile_form.is_valid():
           user2 = user_form.save()
           user2.set_password(user2.password)
           user2.save()
           x = user_form.instance.id
           profile = profile_form.save(commit=False)
           profile_form.instance.user = AuthUser(x)
           if 'profile_pic' in request.FILES:
               profile.profile_pic = request.FILES['profile_pic']
           profile.save()
           return redirect('trip_list')
       else:
           print(user_form.errors)
           print(profile_form.errors)
   else:
      user_form = UserForm
      profile_form = UserProfileForm

   return render(request,'DBapp/edit_profile.html',{'user_form':user_form,'profile_form':profile_form})

#@login_required
#def Update(request,pk):
#   if request.method == 'Post':
#       user_form = UserChangeForm(request.POST, instance=request.user)
#       profile_form = UserProfileChangeForm
#       if form.is_valid():
#           form.save()
#           return redirect('/DBapp/trip_list')
 #  else:
#       user_form = UserChangeForm(instance=request.user)
#       args = {'user_form': form}
#       return render(request,'DBapp/edit_profile.html',args)
