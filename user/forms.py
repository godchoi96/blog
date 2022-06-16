from django import forms

from user.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class JoinForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'nickname']