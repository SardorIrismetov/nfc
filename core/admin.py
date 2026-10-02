from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_active', 'target_url')
    list_filter = ('is_active',)
    search_fields = ('slug', 'target_url')
    list_editable = ('is_active',)
