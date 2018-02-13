from django.conf.urls import url
from django.contrib import admin
from DBapp.api import views

urlpatterns = [
   url(r'^$',views.TripListAPIView.as_view(),name='list'),
   url(r'^(?P<pk>\d+)/$',views.TripDetailAPIView.as_view(),name='detail'),
   url(r'^(?P<pk>\d+)/edit/$',views.TripUpdateAPIView.as_view(),name='update'),
   url(r'^(?P<pk>\d+)/delete/$',views.TripDeleteAPIView.as_view(),name='delete'),
   url(r'^create/$',views.TripCreateAPIView.as_view(),name='create'),
   #url(r'^$',views.TripListView.as_view(),name='trip_list'),
   # matching the primary key to whatever you clicked on:
   #url(r'^trip/(?P<pk>\d+)$',views.TripDetailView.as_view(),name='trip_detail'),
   #url(r'^trip/new/(?P<pk>\d+)$',views.CreateTripView.as_view(),name='trip_new'),
   #url(r'^trip/(?P<pk>\d+)/edit/$',views.TripUpdateView.as_view(),name='trip_edit'),
   #url(r'^trip/(?P<pk>\d+)/remove/$',views.TripDeleteView.as_view(),name='trip_remove'),
   #url(r'^drafts/$',views.DraftListView.as_view(),name='trip_draft_list'),
   #url(r'^trip/(?P<pk>\d+)/comment/$',views.add_comment_to_trip,name='add_comment_to_trip'),
   #url(r'^comment/(?P<pk>\d+)/approve',views.comment_approve,name='comment_approve'),
   #url(r'^comment/(?P<pk>\d+)/remove',views.comment_remove,name='comment_remove'),
   #url(r'^trip/(?P<pk>\d+)/publish',views.trip_publish,name='trip_publish'),
   #url(r'^register/$',views.register,name='register'),
   #url(r'^login/$',views.user_login,name='login'),
]
