from django import forms
from .models import Toffee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ToffeeForm(forms.ModelForm):
    class Meta:
        model = Toffee
        fields = ["title","text","photo"]

class UserRegistrationForm(UserCreationForm):
    email_field = forms.EmailField()
    class Meta():
        model = User
        fields = ('username','email','password1','password2')




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Your Email")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your Message")
