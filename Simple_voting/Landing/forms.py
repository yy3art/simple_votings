from django import forms

class UserForm(forms.Form):
	login = forms.CharField(label="Логин", max_length = 20, min_length = 1, required=True)
	password = forms.CharField(label="Пароль", max_length = 20, min_length = 1, required=True)
