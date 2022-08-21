from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Главная страница тут будет')

def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk} будет тут')
# Create your views here.
