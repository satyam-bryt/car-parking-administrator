from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomSignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'email')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'class': 'form-control'})
        # self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].required = False
        # self.fields['email'].widget.attrs.update({'class': 'form-control'})
