from django.db import models

from intagration_utils_candidate.app_telegram_bot.models.abstract_chat import AbstractChat


class ExampleChat(AbstractChat):
    bot = models.ForeignKey('ExampleBot', on_delete=models.PROTECT)


