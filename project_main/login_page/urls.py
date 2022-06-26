from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),

]