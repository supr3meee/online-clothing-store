from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name='Цена',
        validators=[MinValueValidator(0)]
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    catalog = models.ForeignKey('Catalog', on_delete=models.PROTECT, verbose_name='Каталог')
    # Каталог в кавычках, чтобы не писать его выше Продукта, без кавычек он его не найдет.
    # size = models.ManyToManyField()
    # amount = models.ForeignKey()
    # image = models.ImageField(blank=True)
    # color =
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Вызываем уже в шаблоне под слагом. + надо сделать урл.
        # используется для представления данных из БД. работает в связке с джанго для удобтва использования админпанели.
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta: #используется админ панелью для настройки модели
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['created']


class Catalog(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название каталога')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Вызываем уже в шаблоне под слагом. + надо сделать урл.
        # используется для представления данных из БД. работает в связке с джанго для удобтва использования админпанели.
        return reverse('category', kwargs={'catalog_slug': self.slug})

    class Meta: # используется админ панелью для настройки модели
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"
        ordering = ['id']


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='images/%Y/%m/%d/')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Sizes(models.Model):
    size = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(99)],
        unique=True,
        verbose_name='Размер'
        )

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Amount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='amount')
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, verbose_name='Размер')
    amount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        default=1,
        verbose_name='Количество'
    )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Количество"
        verbose_name_plural = "Количество"
