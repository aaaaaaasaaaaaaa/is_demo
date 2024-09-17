from sympy import trunc

from integration_utils.bitrix_robots.models import BaseRobot
import requests as req


class MyRobot(BaseRobot):
    CODE = 'my_robott'
    NAME = 'Робот возвращает информацию о погоде'
    USE_SUBSCRIPTION = True

    PROPERTIES = {
        'user': {
            'Name': {'ru': 'Получатель'},
            'Value': {'ru': 'Ответственный'},
            'Type': 'user',
            'Required': 'Y',
        },
        'location': {
            'Name': {'ru': 'Город'},
            'Type': 'string',
            'Required': 'Y',
        },
    }

    RETURN_PROPERTIES = {
        'location': {
            'Name': {'ru': 'Город'},
            'Type': 'string',
            'Required': 'Y',
        },
        'current': {
            'Name': {'ru': 'Данные о погоде'},
            'Type': 'string',
            'Required': 'Y',
        },
        'ok': {
            'Name': {'ru': 'ok'},
            'Type': 'bool',
            'Required': 'Y',
        },
        'error': {
            'Name': {'ru': 'error'},
            'Type': 'string',
            'Required': 'N',
        },
    }

    # responce = req.get(f'http://api.weatherapi.com/v1/current.json?key=5c1d9b9bc3134c098ef235146242808&q=Saint%20Petersburg&aqi=no')
    # data = responce.json()
    # print(data)


    def process(self) -> dict:
        try:
            responce = req.get('http://api.weatherapi.com/v1/current.json?key=5c1d9b9bc3134c098ef235146242808&q={}&aqi=no'.format(self.PROPERTIES['location']['Name']))
            data = responce.json()
            self.dynamic_token.call_api_method('bizproc.event.send', {"event_token": self.event_token,
                                                                      "return_values": {"location": data['location']['name'],
                                                                                        "current": data['current'],
                                                                                        }})
            print(data)

        except KeyError:
            self.dynamic_token.call_api_method('bizproc.event.send', {"event_token": self.event_token,
                                                                      "return_values": {"location": ''}})

        except Exception as exc:
            return dict(ok=False, error=str(exc))

        return dict(ok=False)






