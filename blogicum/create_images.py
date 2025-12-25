#!/usr/bin/env python
"""Создание тестовых изображений для постов."""

import os
from PIL import Image, ImageDraw, ImageFont

def create_test_image(filename, text, color, size=(800, 400)):
    """Создает тестовое изображение с текстом."""
    # Создаем изображение
    img = Image.new('RGB', size, color=color)
    draw = ImageDraw.Draw(img)
    
    # Пытаемся использовать системный шрифт
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 40)
        except:
            font = ImageFont.load_default()
    
    # Получаем размеры текста
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Центрируем текст
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Рисуем текст
    draw.text((x, y), text, fill='white', font=font)
    
    # Сохраняем изображение
    img.save(filename)
    print(f"Создано изображение: {filename}")

def main():
    """Создает тестовые изображения."""
    # Создаем директорию если её нет
    os.makedirs('media/posts', exist_ok=True)
    
    # Создаем изображения для разных тем
    images = [
        ('media/posts/django_intro.jpg', 'Django Framework', '#0C4B33'),
        ('media/posts/spb_travel.jpg', 'Санкт-Петербург', '#4A90E2'),
        ('media/posts/healthy_life.jpg', 'Здоровый образ жизни', '#7ED321'),
        ('media/posts/web_dev.jpg', 'Web Development', '#F5A623'),
        ('media/posts/travel_planning.jpg', 'Планирование путешествий', '#BD10E0'),
    ]
    
    for filename, text, color in images:
        create_test_image(filename, text, color)
    
    print("Все тестовые изображения созданы!")

if __name__ == '__main__':
    main()