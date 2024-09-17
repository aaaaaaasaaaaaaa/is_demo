import json
import os
import requests
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from numba.core.tracing import event

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth

APPS_CONFIG = {}

def get_config_file_name(domain):
    return f"config_{domain.replace('.', '_')}.json"

def save_params(params, domain):
    config_file_name = get_config_file_name(domain)
    with open(os.path.join(os.path.dirname(__file__), config_file_name), 'w') as config_file:
        json.dump(params, config_file)

def load_params(domain):
    config_file_name = get_config_file_name(domain)
    config_path = os.path.join(os.path.dirname(__file__), config_file_name)
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    return {}

def rest_command(method, params, auth):
    url = f"https://{auth['domain']}/rest/{method}"
    params['auth'] = auth['access_token']
    response = requests.post(url, data=params)
    return response.json()

def get_answer(command, user_id, auth):
    if command.lower() == 'что горит':
        return b24_bad_tasks(user_id, auth)
    else:
        return {
            'title': 'Туплю-с',
            'report': 'Не соображу, что вы хотите узнать. А может вообще не умею...',
            'attach': []
        }

def b24_bad_tasks(user_id, auth):
    tasks = rest_command('task.item.list', {
        'ORDER': {'DEADLINE': 'desc'},
        'FILTER': {'RESPONSIBLE_ID': user_id, '<DEADLINE': '2024-09-01'},  # Replace with current date
    }, auth)

    if len(tasks['result']) > 0:
        ar_tasks = []
        for task in tasks['result']:
            ar_tasks.append({
                'LINK': {
                    'NAME': task['TITLE'],
                    'LINK': f"https://{auth['domain']}/company/personal/user/{task['RESPONSIBLE_ID']}/tasks/task/view/{task['ID']}/"
                }
            })
            ar_tasks.append({
                'DELIMITER': {
                    'SIZE': 400,
                    'COLOR': '#c6c6c6'
                }
            })
        return {
            'title': 'Да, кое-какие задачи уже пролетели, например:',
            'report': '',
            'attach': ar_tasks
        }
    else:
        return {
            'title': 'Шикарно работаете!',
            'report': 'Нечем даже огорчить - ни одной просроченной задачи',
            'attach': []
        }

def bot_id_finder(name, bot_list):
    for id in bot_list:
        print(bot_list[id]['NAME'])
        if name == bot_list[id]['NAME']:
            bot_id = id
            return bot_id
    return 0



@main_auth(on_start=True, set_cookie=True)
@csrf_exempt
def bot_event_handler(request):
    if request.method == 'POST':
        but = request.bitrix_user_token
        event_data = request.POST
        print('1', event_data)
        event = event_data.get('event')
        # print('4', event, event_data['data[PARAMS][BOT_ID]'])

        if event == 'ONIMBOTMESSAGEADD':

            but.call_api_method('imbot.message.add', {
                'BOT_ID': event_data['data[PARAMS][TO_USER_ID]'],
                "DIALOG_ID": event_data['data[PARAMS][DIALOG_ID]'],
                "MESSAGE": f"Привет, {event_data['data[USER][NAME]']}, Твое сообщение: {event_data['data[PARAMS][MESSAGE]']}",

            })

        elif event == 'ONIMBOTJOINCHAT':
            print('5', event_data['data[PARAMS][BOT_ID]'], event_data['data[PARAMS][USER_ID]'])
            but.call_api_method('imbot.message.add', {
                'BOT_ID': event_data['data[PARAMS][BOT_ID]'],
                'FROM_USER_ID':  event_data['data[PARAMS][BOT_ID]'],
                'TO_USER_ID': event_data['data[PARAMS][USER_ID]'],
                'MESSAGE': 'Привет! Я новый бот!!!.',
            })

        elif event == 'ONIMBOTDELETE':
            but.call_api_method('imbot.unregister', {
                'BOT_ID': event_data['data[PARAMS][BOT_ID]'],
                'CLIENT_ID': event_data['data[PARAMS][BOT_CODE]']
            })

        elif event == 'ONAPPINSTALL':
            print('working1')
            handler_back_url = request.build_absolute_uri()
            but.call_api_method('imbot.register', {
                'CODE': 'New_Test_Bot2',
                'TYPE': 'B',
                'EVENT_MESSAGE_ADD': handler_back_url,
                'EVENT_WELCOME_MESSAGE': handler_back_url,
                'EVENT_BOT_DELETE': handler_back_url,
                'PROPERTIES': {
                    'NAME': 'Тест-бот2',
                    'COLOR': 'AQUA',
                    'EMAIL': 'no@mail.com',
                    'PERSONAL_BIRTHDAY': '2024-09-03',
                    'WORK_POSITION': 'Докладываю о делах',
                    'PERSONAL_GENDER': 'M',
                },
            })

            print('working2')
            name = 'Тест-бот2'
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
            chat_id = chat_id['result']['ID']


            but.call_api_method('imbot.message.add', {
                'BOT_ID': bot_id,
                'DIALOG_ID': chat_id,
                'MESSAGE': 'Привет!',
            })


        return JsonResponse({'status': 'ok'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)


'''
            APPS_CONFIG[auth_token] = {
                'BOT_ID': result['result'],
                'LANGUAGE_ID': event_data['data[LANGUAGE_ID]'],
            }
            save_params(APPS_CONFIG, domain)

'''