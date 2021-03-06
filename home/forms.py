from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea

from .models import Review


# the form for signup
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.DecimalField(
        max_digits=15, decimal_places=0, help_text='Required. Phone Number.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'phone', 'password1', 'password2',)


# the new review form
class ReviewNewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'type', 'content', 'image', ]
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
