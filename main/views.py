from django.shortcuts import render
from .models import Banner

def home_view(request):
    # Получаем все баннеры из базы данных
    banners = Banner.objects.all()
    
    # Отправляем баннеры в шаблон
    return render(request, 'home.html', {'banners': banners})
