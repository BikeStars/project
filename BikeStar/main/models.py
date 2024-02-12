from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Route(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='routes/', null=True, blank=True)
    distance = models.TextField('Расстояние')
    pulsemid = models.TextField('Ср. пульс')
    pulsemin = models.TextField('Мин. пульс')
    pulsemax = models.TextField('Макс. пульс')
    complition_status = models.TextField('Завершённость')
    distance = models.TextField('Расстояние')
    coordinates = models.TextField('Координаты')

    def get_absolute_url(self):
        return reverse('main_detail', kwargs={'pk': self.pk})

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )

    def __str__(self):
        return f"Route(id={self.id}, title={self.title})"

    class Meta:
        db_table = "routes"