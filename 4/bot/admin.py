from django.contrib import admin
from .models import TelegramUser, Message

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name')
    search_fields = ('username', 'first_name', 'user_id')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at')
    search_fields = ('text',)
