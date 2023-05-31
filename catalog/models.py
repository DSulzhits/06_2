from django.db import models

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
    image = models.ImageField(upload_to='image/', verbose_name='изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # обязательно
    price = models.PositiveIntegerField(verbose_name='цена за покупку', **NULLABLE)
    created = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    updated = models.DateField(verbose_name='дата последнего изменения', auto_now=True, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.price}'

    pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
