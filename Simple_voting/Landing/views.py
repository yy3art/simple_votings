from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Landing import models
from Landing.forms import CreateVotingForm
from Landing.models import Voting



def default_menu() -> tuple:
    return (
             {'url': '/', 'text': 'Главная'},
             {'url': '/login/', 'text': 'Авторизация'},
             {'url': '/registr/', 'text': 'Регистрация'},
             {'url': '/vote/', 'text': 'Голосовалка'},
             {'url': '/vote_link/', 'text': 'список голований'},
             {'url': '/create_voting/', 'text': "Создать голосование"}
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
    context = {'page_name': 'Список голосований', 'menu': default_menu(), 'pipka' : [i for i in range(len(models.Voting.objects.all()))]}
    return render(request, 'voting_list.html', context)


def create_voting_page(request):
    context = {'page_name': 'Создать голосование', 'menu': default_menu()}
    context['form'] = CreateVotingForm()
    if request.method == 'POST':
        form = CreateVotingForm(request.POST)
        voting = Voting()
        voting.ans_1 = form['answer1'].value()
        voting.ans_2 = form['answer2'].value()
        voting.question = form['question'].value()
        voting.count_1 = 0
        voting.count_2 = 0
        voting.count_all = 0
        voting.persent_1 = 0.0
        voting.persent_2 = 0.0
        voting.save()
        return redirect('')
    return render(request, 'create_voting.html', context)
