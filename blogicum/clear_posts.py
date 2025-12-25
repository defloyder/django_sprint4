#!/usr/bin/env python
"""Очистка постов и комментариев."""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
django.setup()

from blog.models import Post, Comment

def clear_posts():
    """Удаляет все посты и комментарии."""
    Comment.objects.all().delete()
    Post.objects.all().delete()
    print("Все посты и комментарии удалены!")

if __name__ == '__main__':
    clear_posts()