from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin  # импортируем модель адмдинки


# Register your models here.

# Регистрируем модели для перевода в админке
class CategoryAdmin(TranslationAdmin):
    model = Category


class RecordlAdmin(TranslationAdmin):
    model = Post


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
