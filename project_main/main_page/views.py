from django.shortcuts import render
from .models import Main_page
from project_main.utils import MyMixin  # Import ur Mixin there


def index(request):
    news = Main_page.objects.all()
    return render(request, 'main_page/base_main_page.html', {'title': 'Список говна'})



