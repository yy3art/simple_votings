from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def default_menu() -> tuple:
    return (
             {'url': '/', 'text': 'Главная'},
             {'url': '/login/', 'text': 'Авторизация'},
             {'url': '/registr/', 'text': 'Регистрация'},
             {'url': '/vote/', 'text': 'Голосовалка'},
             {'url': '/vote_link/', 'text': 'список голований'},
    )


def index_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Главная', 'menu': default_menu()}
    return render(request, 'index.html', context)


def authorization_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Авторизация', 'menu': default_menu()}
    return render(request, 'authorization.html', context)


def registration_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Регистрация', 'menu': default_menu()}
    return render(request, 'registr.html', context)


def voting_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Голосовалка', 'menu': default_menu()}
    return render(request, 'voting.html', context)


def voting_spispage(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Список голосований', 'menu': default_menu()}
    return render(request, 'voting_list.html', context)