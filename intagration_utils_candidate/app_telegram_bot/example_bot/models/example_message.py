from django.db import models

from intagration_utils_candidate.app_telegram_bot.models.abstract_message import AbstractMessage


class ExampleMessage(AbstractMessage):
    chat = models.ForeignKey('ExampleChat', on_delete=models.CASCADE, related_name='history')
    author = models.ForeignKey('ExampleUser', on_delete=models.CASCADE, null=True)


