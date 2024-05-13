from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    photo = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['sort']

class Timetable(models.Model):
    day = models.CharField(max_length=255, unique=True)
    opening_hours = models.CharField(max_length=245, unique=False, null=True)

    def __str__(self):
        return f' {self.day}'

    class Meta:
        verbose_name = 'Часы работы'
        verbose_name_plural = 'Часы работы'


