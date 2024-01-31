from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from Landing import forms
from Landing import models

def default_menu() -> tuple:
    return (
             {'url': '/', 'text': 'Главная'},
             {'url': '/login/', 'text': 'Авторизация'},
             {'url': '/register/', 'text': 'Регистрация'},
             {'url': '/vote/', 'text': 'Голосовалка'},
             {'url': '/logout/', 'text': 'Выйти из аккаунта'},
             {'url': '/vote_link/', 'text': 'список голований'},
    )


def index_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Главная', 'menu': default_menu()}
    return render(request, 'index.html', context)

def register(request):
    context = {}
    context['page_name'] = 'Регистрация'
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User(username=username, password=password, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, f'Вы создали аккаунт {username}')
            print(f'username: {user.username}, password: {user.password}')
            return redirect('/')
        else:
            print(form.error_messages)
            return redirect('/register/')
    else:
        form = forms.UserRegistrationForm()
        context['form'] = form
    return render(request, 'registration/registration.html', context)

def login_page(request):
    context = {}
    context['page_name'] = 'Авторизация'
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        username = form.data.get('username')
        password = form.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Авторизация прошла успешно')
            print('Вы вошли в аккаунт')
            return redirect('/')
        else:
            print('unluck', form.data.get('user'), form.data.get('password'))
            messages.add_message(request, messages.ERROR, 'Неправильный логин или пароль')
            return redirect('/login/')
    else:
        form = forms.LoginForm()
        context['form'] = form
    return render(request, 'registration/login.html', context)

def logout_page(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Вы успешно вышли из аккаунта')
    return redirect('/')


@login_required
def voting_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Голосовалка', 'menu': default_menu()}
    return render(request, 'voting.html', context)

def authorization_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Авторизация', 'menu': default_menu()}
    return render(request, 'authorization.html', context)


def voting_spispage(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Список голосований', 'menu': default_menu()}
    return render(request, 'voting_list.html', context)
