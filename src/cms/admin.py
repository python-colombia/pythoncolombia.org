# Django Modules
from django.contrib import admin

# App Modules
from .models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
