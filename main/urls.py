from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views

urlpatterns = [
    path('banners/', views.banners_view, name='banners_view'),  # Страница с баннерами
]

urlpatterns = [
    path('', views.home_view, name='home'),  # Главная страница
]

# Обработка медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
