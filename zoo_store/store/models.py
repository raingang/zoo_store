from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=400, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=200, null=True)
    description = models.CharField(max_length=2000, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    copies = models.IntegerField(
        blank=True, default=0, verbose_name='Количество копий')
    discount = models.IntegerField(
        blank=True, null=True, verbose_name='Скидка')
    created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Дата последнего редактирования')
    image = models.ImageField(
        blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение товара')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    category = models.ForeignKey(Category, null=True, verbose_name='Категория')

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        index_together = ['id', 'slug']

    def __str__(self):
        return self.name
