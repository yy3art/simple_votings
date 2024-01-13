from django import forms



class UserForm(forms.Form):
	login = forms.CharField(label="Логин", max_length = 20, min_length = 1, required=True)
	password = forms.CharField(label="Пароль", max_length = 20, min_length = 1, required=True)
	act = forms.BooleanField(required=True) #true - регистрация, false - вход
	
def register(request):
	if(request.method == 'POST'):
		f = UserForm(request.POST)
		if f.is_valid():
			a = f.data['login']
			b = f.data['password']
			c = f.data['act']
			if(c):	
				item = User(login=a, password=b)
				item.save()
			else:
				data = User.objects.filter(login=a);
				if(data.password = b):
					#Пользователь вошёл
			
