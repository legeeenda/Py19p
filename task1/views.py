from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ContactForm
from django.http import HttpResponse
from .models import Buyer  # Импортируем модель Buyer
from decimal import Decimal
from .models import Game
from .models import News 
from django.core.paginator import Paginator

from django.db import models

def main(request: HttpRequest) -> HttpResponse:
    """Главная страница."""
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'fourth_task/main.html', context)


def cart(request: HttpRequest) -> HttpResponse:
    """Корзина."""
    context = {
        'title': 'Корзина',
    }
    return render(request, 'fourth_task/cart.html', context)


def shop(request: HttpRequest) -> HttpResponse:
    """Магазин."""
    # Получаем все игры из базы данных
    games = Game.objects.all()
    # Количество игр
    numbers_of_games = games.count()

    context = {
        'title': 'Игры',
        'games': games,
        'quantity': numbers_of_games,
    }
    return render(request, 'fourth_task/shop.html', context)


def render_registration_page(request, answer: str, form: ContactForm | None = None) -> HttpResponse:
    """
    Renders the registration page with the given answer and form.
    """
    return render(request, 'fourth_task/registration_page.html', {'answer': answer, 'form': form})


def registration(request: HttpRequest,
                 username: str,
                 password: str,
                 repeat_password: str,
                 age: int,
                 form: ContactForm | None = None) -> HttpResponse:

    # Проверка на совпадение паролей
    if password != repeat_password:
        return render_registration_page(request, 'Пароли не совпадают', form)

    # Проверка возраста
    if age < 18:
        return render_registration_page(request, 'Вы должны быть старше 18 лет', form)

    # Проверка на существование пользователя
    if Buyer.objects.filter(name=username).exists():
        return render_registration_page(request, 'Пользователь с таким именем уже существует', form)

    # Создание нового пользователя
    new_user = Buyer.objects.create(
        name=username,
        balance=Decimal('0.00'),  # Для примера, начальный баланс 0
        age=age
    )

    return render_registration_page(request, f'Приветствуем {username}!', form)


def sign_up_by_html(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        return registration(request, username, password, repeat_password, age)

    return render_registration_page(request, 'Регистрация')


def sign_up_by_django(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            return registration(request, username, password, repeat_password, age, form)

    else:
        form = ContactForm()

    return render_registration_page(request, 'Регистрация', form)






def news(request):
    all_news = News.objects.all()  # Получаем все новости
    paginator = Paginator(all_news, 5)  # Пагинация по 5 новостей на страницу
    page_number = request.GET.get('page')  # Получаем номер страницы из GET параметров
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы для отображения

    return render(request, 'fourth_task/news.html', {'page_obj': page_obj})