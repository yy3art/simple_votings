from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
            }
        )
    )

    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )


class CreateVotingForm(forms.Form):
    question = forms.CharField(
        label='Вопрос',
        required=True
    )
    answer1 = forms.CharField(
        label='Ответ 1',
        required=True
    )
    answer2 = forms.CharField(
        label='Ответ 2',
        required=True
    )

class ViewVotingForm(forms.Form):
    question = ''
    answer1 = ''
    answer2 = ''
    count_1 = 0
    count_2 = 0
    count_all = 0
    persent_1 = 0.0
    persent_2 = 0.0
    author = ''

