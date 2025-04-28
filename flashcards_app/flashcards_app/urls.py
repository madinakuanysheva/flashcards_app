from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.urls')),  # cards отвечает за главную страницу
    path('users/', include('users.urls')),  # users - для регистрации/входа/выхода
]