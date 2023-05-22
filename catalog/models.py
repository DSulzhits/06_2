from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование')  # обязательно
    product_description = models.TextField(verbose_name='описание', **NULLABLE)
    product_image = models.ImageField(verbose_name='изображение(превью)', **NULLABLE)
    product_category = models.CharField(max_length=150, verbose_name='категория')  # обязательно
    product_price = models.IntegerField(verbose_name='цена за покупку')
    product_creation_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    product_last_changes_date = models.DateTimeField(verbose_name='дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.product_name} {self.product_price}'
    pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='наименование')  # обязательно
    category_description = models.TextField(verbose_name='описание', **NULLABLE)

    # category_created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)
