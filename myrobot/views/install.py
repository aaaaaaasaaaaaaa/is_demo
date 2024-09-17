from django.http import HttpResponse

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from myrobot.models.models import MyRobot


@main_auth(on_cookies=True)
def install(request):
    try:
        MyRobot.install_or_update('my_robot:handler_robot', request.bitrix_user_token)
    except Exception as exc:
        return HttpResponse(str(exc))

    return HttpResponse('ok')
