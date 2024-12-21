from django.contrib import admin
from .models import Banner

# Регистрация модели в админке
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  # Поля, которые будут отображаться в списке
    search_fields = ('title', 'description')  # Поиск по этим полям

admin.site.register(Banner, BannerAdmin)
