from django.shortcuts import render

from django.shortcuts import render
from .models import Audio_page


def index(request):
    news = Audio_page.objects.all()
    return render(request, 'audio_page/index.html', {'title': 'Тут будет музыка'})
