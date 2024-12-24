"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from task1.views import main, cart, shop
from task1.views import sign_up_by_html, sign_up_by_django

from task1 import views

urlpatterns = [
    # task 2
    path('admin/', admin.site.urls),
    path('news/', views.news, name='news'),  
    

    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),

    # task 4
    path('', main),
    path('shop/', shop),
    path('cart/', cart),

    # task 5
    path('html', sign_up_by_html),
    path('django', sign_up_by_django),
]


