from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.CharField(label="email", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = Super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return save()



class LoginForm(forms.Form):
    username = forms.CharField(label="username", required=True)
    email = forms.CharField(label="email", required=True)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

