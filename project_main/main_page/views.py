from django.shortcuts import render
from .models import Main_page


def index(request):
    news = Main_page.objects.all()
    return render(request, 'main_page/index.html', {'title': 'Список говна'})

