#!/usr/bin/env python
"""Создание тестовых данных для блога."""

import os
import sys
import django
from datetime import datetime, timedelta

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
django.setup()

from django.contrib.auth import get_user_model
from blog.models import Category, Location, Post, Comment
from django.utils import timezone

User = get_user_model()

def create_test_data():
    """Создание тестовых данных."""
    
    # Создание пользователей
    admin, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'first_name': 'Админ',
            'last_name': 'Администратор',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin.set_password('admin123')
        admin.save()
        print(f"Создан суперпользователь: {admin.username}")
    
    user1, created = User.objects.get_or_create(
        username='blogger1',
        defaults={
            'email': 'blogger1@example.com',
            'first_name': 'Иван',
            'last_name': 'Блогеров'
        }
    )
    if created:
        user1.set_password('password123')
        user1.save()
        print(f"Создан пользователь: {user1.username}")
    
    user2, created = User.objects.get_or_create(
        username='blogger2',
        defaults={
            'email': 'blogger2@example.com',
            'first_name': 'Мария',
            'last_name': 'Писательская'
        }
    )
    if created:
        user2.set_password('password123')
        user2.save()
        print(f"Создан пользователь: {user2.username}")
    
    # Создание категорий
    tech_cat, created = Category.objects.get_or_create(
        slug='tech',
        defaults={
            'title': 'Технологии',
            'description': 'Статьи о современных технологиях и программировании'
        }
    )
    if created:
        print(f"Создана категория: {tech_cat.title}")
    
    travel_cat, created = Category.objects.get_or_create(
        slug='travel',
        defaults={
            'title': 'Путешествия',
            'description': 'Рассказы о путешествиях и интересных местах'
        }
    )
    if created:
        print(f"Создана категория: {travel_cat.title}")
    
    life_cat, created = Category.objects.get_or_create(
        slug='lifestyle',
        defaults={
            'title': 'Образ жизни',
            'description': 'Статьи о здоровом образе жизни и саморазвитии'
        }
    )
    if created:
        print(f"Создана категория: {life_cat.title}")
    
    # Создание локаций
    moscow, created = Location.objects.get_or_create(
        name='Москва',
        defaults={'is_published': True}
    )
    if created:
        print(f"Создана локация: {moscow.name}")
    
    spb, created = Location.objects.get_or_create(
        name='Санкт-Петербург',
        defaults={'is_published': True}
    )
    if created:
        print(f"Создана локация: {spb.name}")
    
    online, created = Location.objects.get_or_create(
        name='Онлайн',
        defaults={'is_published': True}
    )
    if created:
        print(f"Создана локация: {online.name}")
    
    # Создание постов
    posts_data = [
        {
            'title': 'Введение в Django',
            'text': '''Django — это высокоуровневый веб-фреймворк для Python, который способствует быстрой разработке и чистому, прагматичному дизайну.
            
Основные преимущества Django:
• Быстрая разработка
• Безопасность из коробки
• Масштабируемость
• Отличная документация

Django следует принципу DRY (Don't Repeat Yourself) и включает в себя множество готовых компонентов для создания веб-приложений.

Фреймворк предоставляет:
- ORM для работы с базами данных
- Систему шаблонов
- Административную панель
- Систему аутентификации
- Множество встроенных приложений

Начать изучение Django стоит с официальной документации и создания простого проекта.''',
            'author': user1,
            'category': tech_cat,
            'location': online,
            'pub_date': timezone.now() - timedelta(days=5),
            'image': 'posts/django_intro.jpg'
        },
        {
            'title': 'Путешествие в Санкт-Петербург',
            'text': '''Недавно посетил культурную столицу России и остался под большим впечатлением!
            
Что обязательно стоит посетить:
• Эрмитаж - один из крупнейших музеев мира
• Петропавловская крепость - историческое сердце города
• Невский проспект - главная улица города
• Дворцовая площадь - архитектурный ансамбль

Санкт-Петербург действительно заслуживает звания культурной столицы. Каждый уголок города пропитан историей.

Особенно впечатлили:
- Разводные мосты в белые ночи
- Архитектура центра города
- Атмосфера старинных улочек
- Богатство музейных коллекций

Рекомендую планировать поездку минимум на 4-5 дней, чтобы успеть увидеть основные достопримечательности.''',
            'author': user2,
            'category': travel_cat,
            'location': spb,
            'pub_date': timezone.now() - timedelta(days=3),
            'image': 'posts/spb_travel.jpg'
        },
        {
            'title': 'Здоровый образ жизни в большом городе',
            'text': '''Жизнь в мегаполисе накладывает свои ограничения, но это не повод отказываться от здорового образа жизни.
            
Простые правила для горожанина:
• Регулярные прогулки в парках
• Правильное питание несмотря на быстрый ритм
• Достаточный сон (7-8 часов)
• Физическая активность хотя бы 30 минут в день

Главное - найти баланс между работой и отдыхом.

Практические советы:
- Используйте лестницы вместо лифта
- Ходите пешком на короткие расстояния
- Готовьте еду дома
- Проветривайте помещение
- Делайте перерывы в работе

Помните: здоровье - это инвестиция в будущее!''',
            'author': user1,
            'category': life_cat,
            'location': moscow,
            'pub_date': timezone.now() - timedelta(days=1),
            'image': 'posts/healthy_life.jpg'
        },
        {
            'title': 'Основы веб-разработки',
            'text': '''Веб-разработка - это увлекательная область, которая постоянно развивается.
            
Основные технологии:
• HTML - структура веб-страниц
• CSS - стилизация и внешний вид
• JavaScript - интерактивность
• Backend фреймворки (Django, Flask, FastAPI)

Для начинающих рекомендую начать с изучения HTML и CSS, затем переходить к JavaScript и выбранному backend фреймворку.

Этапы изучения:
1. Основы HTML и CSS
2. JavaScript и DOM
3. Выбор backend фреймворка
4. Изучение баз данных
5. Практические проекты

Важно постоянно практиковаться и создавать реальные проекты для портфолио.''',
            'author': user2,
            'category': tech_cat,
            'location': online,
            'pub_date': timezone.now() - timedelta(hours=12),
            'image': 'posts/web_dev.jpg'
        },
        {
            'title': 'Планирование отпуска: советы путешественника',
            'text': '''Хорошо спланированный отпуск - залог отличного отдыха и ярких впечатлений.
            
Этапы планирования:
1. Выбор направления и времени
2. Бронирование жилья и транспорта
3. Составление маршрута
4. Подготовка документов
5. Упаковка багажа

Не забывайте оставлять время для спонтанных открытий - часто именно они становятся самыми яркими воспоминаниями!

Полезные советы:
- Изучите местную культуру заранее
- Выучите несколько фраз на местном языке
- Сделайте копии документов
- Узнайте о местных традициях и обычаях
- Подготовьте аптечку

Главное правило путешественника - будьте открыты к новому опыту!''',
            'author': user1,
            'category': travel_cat,
            'location': moscow,
            'pub_date': timezone.now() - timedelta(hours=6),
            'image': 'posts/travel_planning.jpg'
        }
    ]
    
    created_posts = []
    for post_data in posts_data:
        post, created = Post.objects.get_or_create(
            title=post_data['title'],
            defaults=post_data
        )
        if created:
            created_posts.append(post)
            print(f"Создан пост: {post.title}")
    
    # Создание комментариев
    if created_posts:
        comments_data = [
            {
                'post': created_posts[0],
                'author': user2,
                'text': 'Отличная статья! Django действительно отличный фреймворк для начинающих.'
            },
            {
                'post': created_posts[0],
                'author': admin,
                'text': 'Согласен, Django имеет отличную документацию и активное сообщество.'
            },
            {
                'post': created_posts[1],
                'author': user1,
                'text': 'Спасибо за рекомендации! Обязательно посещу Эрмитаж при следующем визите.'
            },
            {
                'post': created_posts[2],
                'author': user2,
                'text': 'Очень актуальная тема. Добавлю, что важно также следить за качеством воздуха в помещении.'
            }
        ]
        
        for comment_data in comments_data:
            comment, created = Comment.objects.get_or_create(
                post=comment_data['post'],
                author=comment_data['author'],
                text=comment_data['text']
            )
            if created:
                print(f"Создан комментарий к посту: {comment.post.title}")
    
    print("\nТестовые данные успешно созданы!")
    print("\nДанные для входа:")
    print("Суперпользователь: admin / admin123")
    print("Пользователь 1: blogger1 / password123")
    print("Пользователь 2: blogger2 / password123")

if __name__ == '__main__':
    create_test_data()