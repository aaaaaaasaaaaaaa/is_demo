from django.shortcuts import render, HttpResponse

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from settings import NGROK_URL
from integration_utils.bitrix24.models import BitrixUserToken
# Create your views here.

def bot_id_finder(name, bot_list):
    for id in bot_list:
        print(bot_list[id]['NAME'])
        if name == bot_list[id]['NAME']:
            bot_id = id
            return bot_id

    return 0


@main_auth(on_cookies=True)
def register_bot(request):

    but = request.bitrix_user_token
    print('2', but.call_api_method('imbot.bot.list'))
    name = 'Тест'
    bot_list = but.call_api_method('imbot.bot.list')['result']
    bot_id = bot_id_finder(name, bot_list)
    print('|', bot_id)

    if request.method == 'POST':
        print(but.user.id, '||', but.auth_token, '|||', but.get_auth())

        if bot_id == 0:
            handler_back_url = request.build_absolute_uri()
            but.call_api_method('imbot.register', {
                'CODE': 'TestBot',
                'TYPE': 'B',
                'EVENT_MESSAGE_ADD': handler_back_url,
                'EVENT_WELCOME_MESSAGE': handler_back_url,
                'EVENT_BOT_DELETE': handler_back_url,
                'PROPERTIES': {
                    'NAME': 'Тест',
                    'COLOR': 'AQUA',
                    'EMAIL': 'no@mail.com',
                    'PERSONAL_BIRTHDAY': '2024-09-02',
                    'WORK_POSITION': 'Докладываю о делах',
                    'PERSONAL_GENDER': 'M',
                },

            })

            bot_list = but.call_api_method('imbot.bot.list')['result']
            bot_id = bot_id_finder(name, bot_list)
            print(bot_list)
            print('||', bot_id)


            but.call_api_method('imbot.chat.add', {
                'TYPE': 'CHAT',
                'TITLE': 'Тестовый чат',
                'MESSAGE': 'Создан новый чат',
                'USERS': (int(bot_id), but.user.id),
                'ENTITY_TYPE': 'CHAT',
                'ENTITY_ID': int(bot_id),
                'OWNER_ID': but.user.id,
                'BOT_ID': int(bot_id),

            })
            chat_id = but.call_api_method('imbot.chat.get', {
                'ENTITY_TYPE': 'CHAT',
                'ENTITY_ID': int(bot_id),
                'BOT_ID': int(bot_id),

            })


            user_list = but.call_api_method('imbot.chat.user.list', {
                'CHAT_ID': chat_id['result']['ID'],
                'BOT_ID': int(bot_id),
            })




            return HttpResponse(f'Бот создан, chat_id: {chat_id}, id юзеров: {user_list}')


        if int(bot_id) > 0:
            chat_id = but.call_api_method('imbot.chat.get', {
                'ENTITY_TYPE': 'CHAT',
                'ENTITY_ID': int(bot_id),
                'BOT_ID': int(bot_id),

            })
            chat_id = chat_id['result']['ID']
            but.call_api_method('imbot.message.add', {
                'BOT_ID': bot_id,

                "DIALOG_ID": chat_id,  # but.user.id

                "MESSAGE": 'Привет, удаляю бота',

            })


            but.call_api_method('imbot.unregister', {
                'BOT_ID': bot_id,
                'CLIENT_ID': chat_id
            })
            return HttpResponse('Удален')

    return render(request, 'register_bot.html')

'''
        chat_id = but.call_api_method('imbot.chat.get', {
            'ENTITY_TYPE': 'CHAT',
            'ENTITY_ID': int(bot_id),
            'BOT_ID': int(bot_id),

        }, but.auth_token)
        chat_id = chat_id['result']['ID']

        if event == 'ONIMBOTMESSAGEADD':
            if not auth['application_token']:
                return HttpResponse('Ошибка')
            report = "Сообщение"

            but.call_api_method('imbot.message.add', {
                "DIALOG_ID": chat_id,
                "MESSAGE": f"{report['title']}\n{report['report']}\n",
                "ATTACH": report['attach']
            }, auth)


        elif event == 'ONIMBOTJOINCHAT':
            if not auth['application_token']:
                return HttpResponse('Ошибка')
            report = "Сообщение"

            but.call_api_method('imbot.message.add', {
                "DIALOG_ID": chat_id,
                "MESSAGE": f"{report['title']}\n{report['report']}\n",
                "ATTACH": report['attach']
            }, auth)

        elif event == 'ONIMBOTDELETE':
            but.call_api_method('imbot.unregister', {
                'BOT_ID': bot_id,
                'CLIENT_ID': but.user.id
            }, but.auth_token)


        elif event == 'ONAPPINSTALL':
            handler_back_url = request.build_absolute_uri()
            but.call_api_method('imbot.register', {
                'CODE': 'TestBot',
                'TYPE': 'B',
                'EVENT_MESSAGE_ADD': handler_back_url,
                'EVENT_WELCOME_MESSAGE': handler_back_url,
                'EVENT_BOT_DELETE': handler_back_url,
                'PROPERTIES': {
                    'NAME': 'Тест',
                    'COLOR': 'AQUA',
                    'EMAIL': 'no@mail.com',
                    'PERSONAL_BIRTHDAY': '2024-09-02',
                    'WORK_POSITION': 'Докладываю о делах',
                    'PERSONAL_GENDER': 'M',
                },

            }, but.auth_token)


    return render(request, 'register_bot.html')





but.call_api_method('imbot.message.add', {
                'BOT_ID': bot_id,

                "FROM_USER_ID": 'TO_USER_ID',  # but.user.id

                "MESSAGE": 'Привет, удаляю бота',

            }, )

            but.call_api_method('imbot.unregister', {
                'BOT_ID': bot_id,
                'CLIENT_ID': but.user.id
            })

            HttpResponse('Бот удален')

        event_data = request.POST
        event = event_data.get('event')
        print(event)
        return HttpResponse('NOthing')
        
        
        if event == 'ONIMBOTMESSAGEADD':
            but.call_api_method('imbot.message.add', {

                "DIALOG_ID": event_data['data']['PARAMS']['DIALOG_ID'], #  but.user.id

                "MESSAGE": 'Привет',

            },)

        elif event == 'ONIMBOTDELETE':
            but.call_api_method('imbot.message.delete', {

                "DIALOG_ID": event_data['data']['PARAMS']['DIALOG_ID'],  # but.user.id

                "MESSAGE": 'Привет',

            }, )

        return HttpResponse('ok')


    return render(request,'register_bot.html')

'''