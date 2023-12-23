from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def default_menu() -> tuple:
    return (
             {'url': '/', 'text': 'Главная'},
             {'url': '/vote/', 'text': 'Голосовалка'}
    )


def index_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Главная', 'menu': default_menu()}
    return render(request, 'index.html', context)


def voting_page(request: HttpRequest) -> HttpResponse:
    context = {'page_name': 'Голосовалка', 'menu': default_menu()}
    return render(request, 'voting.html', context)

