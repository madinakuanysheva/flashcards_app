import json
import requests
import ast
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Card
from django.contrib.auth.decorators import login_required
from .models import GeneratedTopic, GeneratedCard


API_KEY = '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'
BASE_URL = 'https://api.groq.com/openai/v1/chat/completions'




def index(request):
    return render(request, 'cards/index.html')


def popular_cards(request):
    topics = Topic.objects.all()
    return render(request, 'cards/popular_cards.html', {'topics': topics})


def topic_cards(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    cards = Card.objects.filter(topic=topic)
    return render(request, 'cards/study_topic.html', {'topic': topic, 'cards': cards})

@login_required
def generate_cards(request):
    cards = None
    topic = None  # Чтобы отобразить выбранную тему на странице

    if request.method == 'POST':
        topic_name = request.POST.get("topic")

        if not topic_name:
            return render(request, 'cards/generate_cards.html', {'error_message': 'Тема не была указана'})

        print(f"Тема для генерации: {topic_name}")

        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        }

        payload = {
            "model": "llama-3.3-70b-versatile",  # Используемая модель
            "messages": [
                {"role": "system", "content": "Ты — помощник, который создаёт карточки с вопросами и ответами."},
                {"role": "user", "content": f"Создай 10 карточек с вопросами и ответами по теме '{topic_name}'. Формат ответа: [{{'question': '...', 'answer': '...'}}]"}
            ],
            "n": 1
        }

        try:
            response = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                data = response.json()

                # Попробуем распарсить карточки
                cards_response = data.get('choices', [])[0].get('message', {}).get('content', '')

                if cards_response:
                    try:
                        # Преобразуем строку в список словарей с помощью ast.literal_eval
                        cards = ast.literal_eval(cards_response)
                    except (SyntaxError, ValueError) as e:
                        print(f"Ошибка при распарсивании данных: {e}")
                        cards = []

                if not cards:
                    return render(request, 'cards/generate_cards.html', {'error_message': 'Карточки не были сгенерированы.'})

                # Создаем сгенерированную тему для текущего пользователя
                generated_topic = GeneratedTopic.objects.create(user=request.user, topic=topic_name)

                # Сохраняем карточки, привязывая их к теме
                for card_data in cards:
                    GeneratedCard.objects.create(
                        topic=generated_topic,
                        question=card_data['question'],
                        answer=card_data['answer']
                    )

                return render(request, 'cards/generate_cards.html', {'cards': cards, 'topic': topic_name})

            else:
                return render(request, 'cards/generate_cards.html', {'error_message': f'Ошибка API: {response.text}'})

        except Exception as e:
            return render(request, 'cards/generate_cards.html', {'error_message': f'Ошибка: {str(e)}'})

    return render(request, 'cards/generate_cards.html')

def my_topics(request):
    topics = Topic.objects.all()  # или другой запрос к вашей модели
    return render(request, 'cards/my_topics.html', {'topics': topics})


@login_required
def generated_topics(request):
    topics = GeneratedTopic.objects.filter(user=request.user)  # Получаем все сгенерированные темы для текущего пользователя
    return render(request, 'cards/genarated_topics.html', {'topics': topics})

def study_generated_cards(request, topic_id):
    topic = get_object_or_404(GeneratedTopic, id=topic_id)
    cards = GeneratedCard.objects.filter(topic=topic)
    return render(request, 'cards/study_generated_cards.html', {'topic': topic, 'cards': cards})
