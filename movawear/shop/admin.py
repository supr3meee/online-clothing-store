from django.contrib import admin

from shop.models import *

# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # Содержит список тех полей которые мы хотим видеть в админ панели
    list_display_links = ('id', )
    # Содержит список тех полей на которые можно кликнуть и перейти на соответсвующий объект
    search_fields = ('name', )
    list_editable = ('name', )
    list_filter = ()
    prepopulated_fields = {'slug': ('name', )}
    #


admin.site.register(Catalog, CatalogAdmin)


class ImagesInline(admin.TabularInline):
    fk_name = 'product'
    model = Images


class SizesAdmin(admin.ModelAdmin):
    list_display = ('size', )


admin.site.register(Sizes, SizesAdmin)


class AmountInline(admin.TabularInline):
    fk_name = 'product'
    model = Amount


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, AmountInline, ]
    list_display = ('id', 'name', 'price', 'created', 'updated', 'is_published', 'available', 'catalog')
    #Содержит список тех полей которые мы хотим видеть в админ панели
    list_display_links = ('id', )
    # Содержит список тех полей на которые можно кликнуть и перейти на соответсвующий объект
    search_fields = ('name', )
    # Содержит список тех полей по которым мы можем выполнить поиск информации
    list_editable = ('name', 'price', 'is_published', 'available', 'catalog')
    # Содержит список тех полей на которые можно редактировать
    list_filter = ('is_published', 'available', 'created', 'catalog')
    prepopulated_fields = {'slug': ('name', )}

