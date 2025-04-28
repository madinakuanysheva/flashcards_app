from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.index, name='index'),
    path('popular/', views.popular_cards, name='popular_cards'),
    path('topic/<int:topic_id>/', views.topic_cards, name='topic_cards'),

    path('my_topics/', views.my_topics, name='my_topics'),  # Страница с темами
    path('generate_cards/', views.generate_cards, name='generate_cards'),  # Страница генерации карточек
]
