from django.contrib import admin
from .models import Category, Product, Article, Partner, Company, FAQ, Employee, PrivacyPolicy, Vacancy

# Регистрация для Главной
admin.site.register(Article)
admin.site.register(Partner)
admin.site.register(Company)
admin.site.register(FAQ)
admin.site.register(Employee)
admin.site.register(PrivacyPolicy)
admin.site.register(Vacancy)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
