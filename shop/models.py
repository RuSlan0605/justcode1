from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    geo = models.ImageField()
    def __str__(self):
        return f'{self.title} {self.__class__.__name__}'

    class Meta:
        verbose_name_plural = 'Магазин'
        verbose_name = 'Маркет'
        ordering = '-published',

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name} {self.__class__.__name__}'

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрики'
        ordering = ['name']

