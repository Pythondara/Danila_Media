from django.shortcuts import render

from django.shortcuts import render
from .models import Profile_page


def index(request):
    news = Profile_page.objects.all()
    return render(request, 'profile_page/base_profile_page.html', {'title': 'Тут будет профиль'})