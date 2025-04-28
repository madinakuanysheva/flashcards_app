from django.contrib import admin
from .models import Topic, Card
from .models import GeneratedTopic, GeneratedCard

class GeneratedCardInline(admin.TabularInline):
    model = GeneratedCard
    extra = 1  # Количество пустых форм для добавления карточек

class GeneratedTopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'created_at')  # Отображаем поля на списочной странице
    search_fields = ('topic', 'user__username')  # Делаем поиск по теме и пользователю
    inlines = [GeneratedCardInline]  # Встраиваем карточки в редактор темы

admin.site.register(GeneratedTopic, GeneratedTopicAdmin)
admin.site.register(GeneratedCard)
admin.site.register(Topic)
admin.site.register(Card)
