from django import forms
from django.contrib.auth.models import User
from reg_app.models import UserPorfileInfo,Post

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserPorfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserPorfileInfo
        fields = ('portfolio_site','profile_pic')

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')
