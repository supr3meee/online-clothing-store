from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from shop.models import *


# Create your views here.

menu = [
    {'title': 'Каталог', 'url_name': 'catalog'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Корзина', 'url_name': 'cart_detail'},
    {'title': 'Регистрация', 'url_name': 'register'},
]


class ShopHomeView(ListView):# ВАЖНО тут модель не используется. передлать
    model = Product
    template_name = "shop/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context


class CatalogView(ListView):
    model = Catalog
    template_name = "shop/catalog.html"
    context_object_name = 'catalogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Каталог'
        catalogs = Catalog.objects.annotate(Count('product'))
        #держит в себе значение сколько продуктов есть у той или иной категории
        context['catalogs'] = catalogs
        return context


def about(request):
    context = {
        'menu': menu,
        'title': 'О нас'
    }
    return render(request, "shop/about.html", context=context)


def delivery(request):
    context = {
        'menu': menu,
        'title': 'Доставка'
    }
    return render(request, "shop/delivery.html", context=context)


def cart(request):
    context = {
        'menu': menu,
        'title': 'Корзина'
    }
    return render(request, "cart/detail.html", context=context)


def register(request):
    context = {
        'menu': menu,
        'title': 'Регистрация'
    }
    return render(request, "shop/register.html", context=context)


class ShowProductView(DetailView):
    model = Product
    template_name = "shop/show_product.html"
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Каталог'
        context['cart_product_form'] = CartAddProductForm()
        return context


class ShowCategoryView(ListView):# если набрать несуществующую кат то не вылазит 404
    model = Catalog
    template_name = "shop/show_category.html"
    context_object_name = 'catalogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Каталог'
        context['catalog_slug'] = self.kwargs['catalog_slug']
        catalogs = Catalog.objects.annotate(Count('product'))
        #держит в себе значение сколько продуктов есть у той или иной категории
        context['catalogs'] = catalogs
        return context


def example(request, example_flag):
    return HttpResponse(f"Страница с модулем ре <p>{example_flag}<p/>")


def page_not_found(request, exception):
    return redirect('home', permanent=True)  # Перенаправление на домашнюю страницу при 404
