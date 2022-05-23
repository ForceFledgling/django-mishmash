from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    priority = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "категории"
        verbose_name_plural = "Категории"


class Page(models.Model):
    name = models.CharField(max_length=115, unique=True, verbose_name="Название страницы")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default=1, verbose_name="Категория")
    content = RichTextUploadingField(blank=True, null=True, default='', verbose_name="Контент")
    date_publish = models.DateTimeField(null=True, verbose_name="Дата публикации", blank=True)
    date_edit = models.DateTimeField(null=True, verbose_name="Последнее редактирование", blank=True)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def save(self, *args, **kwargs):
        '''Автоматически обновляем дату редактирования при сохранении и создании'''
        if self.date_publish is None:
            self.date_publish = datetime.now()
        self.date_edit = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "страницы"
        verbose_name_plural = "Страницы"

    def get_absolute_url(self):
        return '/wiki/%i/' % self.id
