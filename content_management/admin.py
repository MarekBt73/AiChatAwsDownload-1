from django.contrib import admin
from .models import Subject, DifficultyLevel, EducationalMaterial, Video, Article, Ebook

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    verbose_name = "Przedmiot"
    verbose_name_plural = "Przedmioty"

@admin.register(DifficultyLevel)
class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    search_fields = ('level',)
    list_display_links = ('level',)
    verbose_name = "Poziom Trudności"
    verbose_name_plural = "Poziomy Trudności"

@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'material_type', 'subject', 'difficulty_level', 'created_at')
    list_filter = ('material_type', 'subject', 'difficulty_level', 'created_at')
    search_fields = ('title', 'description', 'content')
    ordering = ('-created_at',)
    list_display_links = ('title',)
    verbose_name = "Materiał Edukacyjny"
    verbose_name_plural = "Materiały Edukacyjne"

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty_level', 'url', 'created_at')
    list_filter = ('subject', 'difficulty_level', 'created_at')
    search_fields = ('title', 'description', 'url')
    ordering = ('-created_at',)
    list_display_links = ('title',)
    verbose_name = "Wideo"
    verbose_name_plural = "Wideo"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty_level', 'created_at')
    list_filter = ('subject', 'difficulty_level', 'created_at')
    search_fields = ('title', 'description', 'content')
    ordering = ('-created_at',)
    list_display_links = ('title',)
    verbose_name = "Artykuł"
    verbose_name_plural = "Artykuły"

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty_level', 'file', 'created_at')
    list_filter = ('subject', 'difficulty_level', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_display_links = ('title',)
    verbose_name = "Ebook"
    verbose_name_plural = "Ebooki"
