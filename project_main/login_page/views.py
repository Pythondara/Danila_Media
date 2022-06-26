from django.shortcuts import render, redirect
from .models import Login_page
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserRegisterForm
from django.contrib import messages


class LoginView(ListView):
    model = Login_page
    template_name = 'login_page/base_login_page.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'login_page/register.html', {'form': form})


def login(request):
    return render(request, 'login_page/login.html')





