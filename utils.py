import random

def random_color():
    """Возвращает случайный цвет RGB"""
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))

def format_time(seconds):
    """Форматирует время в мм:сс"""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"