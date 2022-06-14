from django.shortcuts import render

from django.shortcuts import render
from .models import Profile_page


def index(request):
    news = Profile_page.objects.all()
    return render(request, 'profile_page/index.html', {'title': 'Тут будет профиль'})