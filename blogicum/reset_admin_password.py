#!/usr/bin/env python
"""Сброс пароля администратора."""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def reset_admin_password():
    """Сбрасывает пароль администратора."""
    try:
        admin = User.objects.get(username='admin')
        admin.set_password('admin123')
        admin.save()
        print("✅ Пароль администратора успешно сброшен!")
        print("Данные для входа:")
        print("Логин: admin")
        print("Пароль: admin123")
    except User.DoesNotExist:
        print("❌ Пользователь admin не найден!")
        print("Создаем нового суперпользователя...")
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print("✅ Суперпользователь создан!")
        print("Данные для входа:")
        print("Логин: admin")
        print("Пароль: admin123")

if __name__ == '__main__':
    reset_admin_password()