import random

from django.shortcuts import render
from django.utils import timezone

from .quotes import QUOTES

WEEKDAYS = [
    'Понеділок',
    'Вівторок',
    'Середа',
    'Четвер',
    "П'ятниця",
    'Субота',
    'Неділя',
]


def index(request):
    today = timezone.localtime()
    context = {
        'weekday': WEEKDAYS[today.weekday()],
        'quote': random.choice(QUOTES),
    }
    return render(request, 'main/index.html', context)
