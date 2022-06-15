from django.shortcuts import render

from django.shortcuts import render
from .models import Video_page


def index(request):
    news = Video_page.objects.all()
    return render(request, 'video_page/base_video_page.html', {'title': 'Тут будет видео'})