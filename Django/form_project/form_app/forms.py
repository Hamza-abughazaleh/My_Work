from django import forms

class Form_Name(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
