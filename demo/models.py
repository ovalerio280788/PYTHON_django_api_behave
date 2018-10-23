from decimal import Decimal

from django.db import models


# Create your models here.
from rest_framework.compat import MinValueValidator


class Home(models.Model):
    home_name = models.CharField(max_length=10, unique=True)
    location = models.TextField(max_length=150)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'

    def __str__(self):
        return self.home_name


class HomeSections(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Home section'
        verbose_name_plural = 'Home sections'

    def __str__(self):
        return self.section_name


class Articles(models.Model):
    section = models.ForeignKey(HomeSections, on_delete=models.CASCADE)
    article_name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    quantity = models.IntegerField(validators=[
        MinValueValidator(Decimal('0')),
    ], default=0)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Home section article'
        verbose_name_plural = 'Home section articles'

    def __str__(self):
        return self.article_name
