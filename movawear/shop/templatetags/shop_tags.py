from django import template
from shop.models import *

register = template.Library()

#Превращаем нашу функцию в тег, путем связывания функции с декоратором. Декоратор принимает
# в себя именованный параметр name='getproduct' и через {% getproduct as products %}
# можем обращаться к данным из модели в html шаблоне


@register.simple_tag()
def get_products():
    return Product.objects.all()





# НУЖНО создать тег, который будет возвращать список отфильтрованных продуктов
# ( скорей всего нужен включающий тег, который сразу будет возвращать html страницу)


@register.inclusion_tag('shop/show_products.html')
def show_products_tag(catalog_slug=None):
    if catalog_slug is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(catalog__slug=catalog_slug)
        # ВАЖНО! тут мы ставим условие: Нам нужны все экз класа Product
        # у которых каталог (атрибут класса Продукт,
        # который хранит в себе экземпляр класса Catalog)
        # имеет слаг равный параметру который мы передаем
    return {'products': products}
