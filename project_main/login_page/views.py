from django.shortcuts import render
from .models import Login_page


def index(request):
    news = Login_page.objects.all()
    return render(request, 'login_page/base_login_page.html', {'title': 'Тут будет логин пейдж'})