from django.contrib import admin
from .models import About, Skills

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'skills_name')
    list_display_links = ('id', 'skills_name')