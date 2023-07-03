from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'phone_number')

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if phone and (len(phone) != 10 or not phone.isdigit()):
            raise forms.ValidationError("Phone number should contain exactly 10 digits.")
        return phone


class LoginForm(forms.Form):
    username = forms.CharField(label='Email or Phone Number')
    password = forms.CharField(widget=forms.PasswordInput)
