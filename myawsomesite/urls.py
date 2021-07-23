"""myawsomesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from news.views import news, news_detail, news_new, tag_detail_view
from products.views import products, products_detail, new_product, new_tag
from userinfo.views import new_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', news, name='news'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('news/tag/<int:pk>/', tag_detail_view, name='news_by_tag'),
    path('news/add/', news_new, name='news_add'),
    path('', new_user, name='add_user'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
    path('products/add', new_product, name='new_product'),
    path('products/tag/add', new_tag, name='new_tag')
]
