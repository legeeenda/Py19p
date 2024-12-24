from django.db import models
from decimal import Decimal

class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя (username)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс покупателя
    age = models.IntegerField()  # Возраст покупателя

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание игры
    age_limited = models.BooleanField(default=False)  # Ограничение по возрасту 18+
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели, обладающие игрой

    def __str__(self):
        return self.title






class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

