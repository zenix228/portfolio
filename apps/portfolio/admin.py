from django.contrib import admin
from .views import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'country', 'link')
    list_display_links = ('id', 'title', 'name', 'country', 'link')