from django.contrib import admin

from .models import MasterChef, ProductType, FoodMenu, TableOnline, Costumer, Testimonial, Contact, Service
from import_export.admin import ImportExportModelAdmin


@admin.register(MasterChef)
class MasterChefAdmin(ImportExportModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    list_filter = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    ordering = ('id',)


@admin.register(ProductType)
class ProductTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')
    ordering = ('id',)


@admin.register(FoodMenu)
class FoodMenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('title', 'description')
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)


@admin.register(TableOnline)
class TableOnlineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'ism', 'email')
    list_filter = ('ism', 'email')
    search_fields = ('id', 'ism', 'email')
    ordering = ('id',)


@admin.register(Costumer)
class CostumerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'last_name')
    list_filter = ('last_name',)
    search_fields = ('id', 'last_name')
    ordering = ('id',)


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin):
    list_display = ('id', 'description', 'costumer')
    list_filter = ('description', 'costumer')
    search_fields = ('id', 'description', 'costumer')
    ordering = ('id',)


@admin.register(Contact)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'email')
    list_filter = ('first_name', 'email')
    search_fields = ('id', 'first_name', 'email')
    ordering = ('id',)


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('title', 'description')
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)
