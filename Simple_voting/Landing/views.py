from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from forms import UserForm
from models import User

def default_menu() -> tuple:
    return (
             {'url': '/', 'text': 'Главная'},
             {'url': '/login/', 'text': 'Авторизация'},
             {'url': '/registr/', 'text': 'Регистрация'},
             {'url': '/vote/', 'text': 'Голосовалка'},
    )


def index_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Главная', 'menu': default_menu()}
    return render(request, 'index.html', context)

def register(request):
    if(request.method == 'POST'):
        f = UserForm(request.POST)
        if f.is_valid():
            a = f.data['login']
            b = f.data['password']
            u = User(login=a, password=b)
            u.save()



def authorization_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Авторизация', 'menu': default_menu()}
    return render(request, 'authorization.html', context)



def registration_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Регистрация', 'menu': default_menu()}
    return render(request, 'registr.html', context)


def voting_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Голосовалка', 'menu': default_menu()}
    return render(request, 'voting.html', context)