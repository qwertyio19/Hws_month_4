from django.db import models
from django.db import models
# Create your models here.


class Banner(models.Model):
    # Заголовок баннера
    title = models.CharField(max_length=255)
    
    # Описание баннера
    description = models.TextField()
    
    # Изображение баннера
    image = models.ImageField(upload_to='banners/')
    
    def __str__(self):
        return self.title
