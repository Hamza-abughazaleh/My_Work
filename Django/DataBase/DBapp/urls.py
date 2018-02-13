from django.conf.urls import url
from DBapp import views
from django.conf.urls.static import static
from DataBase import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url(r'^index/$',views.IndexView.as_view(),name='index'),
   url(r'^$',views.TripListView.as_view(),name='trip_list'),
   # matching the primary key to whatever you clicked on:
   url(r'^trip/(?P<pk>\d+)$',views.TripDetailView.as_view(),name='trip_detail'),
   url(r'^trip/new/(?P<pk>\d+)$',views.CreateTripView.as_view(),name='trip_new'),
   url(r'^trip/(?P<pk>\d+)/edit/$',views.TripUpdateView.as_view(),name='trip_edit'),
   url(r'^trip/(?P<pk>\d+)/remove/$',views.TripDeleteView.as_view(),name='trip_remove'),
   url(r'^drafts/$',views.DraftListView.as_view(),name='trip_draft_list'),
   url(r'^trip/(?P<pk>\d+)/comment/$',views.AddCommentToTrip.as_view(),name='AddCommentToTrip'),
   url(r'^comment/(?P<pk>\d+)/approve',views.comment_approve,name='comment_approve'),
   url(r'^comment/(?P<pk>\d+)/remove',views.comment_remove,name='comment_remove'),
   url(r'^comment/(?P<pk>\d+)/edit/$',views.CommentUpdateView.as_view(),name='comment_edit'),
   url(r'^trip/(?P<pk>\d+)/publish',views.trip_publish,name='trip_publish'),
   url(r'^register/$',views.register,name='register'),
   url(r'^login/$',views.user_login,name='login'),
   url(r'^trip/(?P<pk>\d+)/vote/$',views.votesys,name='vote'),
   url(r'profile/(?P<pk>\d+)$', views.get_user_profile, name ='get_user_profile'),
   url(r'profile/(?P<pk>\d+)/edit/$',views.Update, name ='profile_edit'),
   url(r'profile/image/(?P<pk>\d+)/edit/$',views.ProfileimageUpdateView.as_view(), name ='profile_image_edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns+= staticfiles_urlpatterns()
