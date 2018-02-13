from django import forms
from DBapp.models import Prize,Userprize,Trip,Votes,Stories,Tripcomment,UserProfile
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

class TripForm(forms.ModelForm):

   class Meta():

       model = Trip
       fields = ('date','title','text')
       widgets = {
           'title':forms.TextInput(attrs={'class':'textinputclass'}),
           'text':forms.Textarea(attrs={'class':'editable medium-editors-textarea tripcontent'}),
           'user':forms.HiddenInput()
       }

   def clean_date(self):
       date = self.cleaned_data['date']
       if date > datetime.date.today():
           raise forms.ValidationError("Enter a valid date")
       return date

class StoryForm(forms.ModelForm):
   class Meta():
       model = Stories
       fields = ('date','stories')

       widgets = {
           'stories':forms.Textarea(attrs={'class':'editable medium-editors-textarea'})
       }

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  confirm_password=forms.CharField(widget=forms.PasswordInput())

  class Meta():
      model = User
      fields = ('username','first_name','last_name','email','password')

  def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

        """Validates that a password is as least 10 characters long and has at least
        2 digits and 1 Upper case letter.
        """
        min_length = 8
        if len(password) < min_length:
             raise ValidationError(('Password must be at least {0} characters '
                                     'long.').format(min_length))

         # check for 2 digits
        if sum(c.isdigit() for c in password) < 2:
             raise ValidationError(('Password must container at least 2 digits.'))

         # check for uppercase letter
        if not any(c.isupper() for c in password):
             raise ValidationError(('Password must container at least 1 uppercase letter.'))



class UserProfileForm(forms.ModelForm):
    class Meta():
        model =UserProfile
        fields = ('profile_pic',)


class Tripcommentform(forms.ModelForm):
    class Meta():
        model = Tripcomment
        fields = ('comment',)
        widgets = {
            'comment':forms.Textarea(attrs={'class':'editable medium-editors-textarea tripcontent'}),
        }
