from django.conf.urls import url
from reg_app import views

app_name = 'reg_app'

urlpatterns = [
        url(r'^register/$',views.register,name='register'),
        url(r'^user_login/$',views.user_login,name='user_login'),

]
