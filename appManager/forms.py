from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.core.validators import MaxValueValidator
from .models import Profile
class RegistrationForm (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    hometown=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Age' }),validators=[MaxValueValidator(99)])
    gender=forms.ChoiceField(choices=Profile.GENDER,widget=forms.Select(attrs={'class':'form-control','placeholder':'Genre'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2','hometown','age','gender')
        
class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username Here', 'class':'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))
