from django.shortcuts import render

from django.shortcuts import render
from .models import History_page


def index(request):
    news = History_page.objects.all()
    return render(request, 'history_page/base_history_page.html', {'title': 'Тут будет история просмотров'})