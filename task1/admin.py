from django.contrib import admin
from .models import Game, Buyer
from .models import News



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение по количеству записей на странице

# Админ-класс для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    list_display = ('name', 'balance', 'age')  # Отображение полей name, balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение по количеству записей на странице
    readonly_fields = ('balance',)  # Сделать поле balance доступным только для чтения




class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  
    list_filter = ('created_at',) 


admin.site.register(News, NewsAdmin)