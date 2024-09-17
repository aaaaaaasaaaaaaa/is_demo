from django.urls import path

from .views.bot_register import register_bot
from .views.bot_handler import bot_event_handler

urlpatterns = [
    path('register_bot/', register_bot, name='register_bot'),
    path('bot_handler/', bot_event_handler, name='bot_handler'),
]
