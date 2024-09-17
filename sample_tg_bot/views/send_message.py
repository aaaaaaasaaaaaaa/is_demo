from django.shortcuts import render
import os
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth

from integration_utils.vendors.telegram import Bot
from local_settings import TG_KEY

@main_auth(on_cookies=True)
def send_message(request):
    if request.method == 'POST':
        bot_token = TG_KEY
        chat_id = request.POST.get('chat_id')
        message_text = request.POST.get('message_text')
        bot = Bot(token=bot_token)
        bot.send_message(text=message_text, chat_id=chat_id)
        bot.sendDice(chat_id=chat_id)

    return render(request, 'msg_input.html')
