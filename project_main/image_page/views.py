from django.shortcuts import render

from django.shortcuts import render
from .models import Image_page


def index(request):
    news = Image_page.objects.all()
    return render(request, 'image_page/base_image_page.html', {'title': 'Тут будут картинки'})