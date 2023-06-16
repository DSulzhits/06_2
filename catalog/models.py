from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')  # обязательно
    description = models.TextField(verbose_name='описание', **NULLABLE)

    # category_created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')  # обязательно
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='images/products/', verbose_name='изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')  # обязательно
    price = models.PositiveIntegerField(verbose_name='цена за покупку')
    created = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    updated = models.DateField(verbose_name='дата последнего изменения', auto_now=True, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    sign_of_current_version = models.BooleanField(default=False, verbose_name='активный')

    def __str__(self):
        return f'{self.product} {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('number',)


class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=300, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/records/', verbose_name='изображение(превью)', **NULLABLE)
    created = models.DateField(verbose_name='дата создания', auto_now_add=True)
    sign_of_publication = models.BooleanField(default=True, verbose_name='активный')
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}, {self.created}"

    def get_absolute_url(self):
        return reverse('catalog:blog_record_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        get_latest_by = 'created'

    def views_count(self):
        self.views += 1
        self.save()
