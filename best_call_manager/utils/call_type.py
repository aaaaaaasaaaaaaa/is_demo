def get_call_type(call):
    """Позволяет распарсить тип звонка и вернуть пользователя описание типа
    звонка в строчном формате"""

    call_types = {
        '1': 'Исходящий',
        '2': 'Входящий',
        '3': 'Входящий с перенаправлением',
        '4': 'Обратный звонок',
    }

    return call_types[call]
