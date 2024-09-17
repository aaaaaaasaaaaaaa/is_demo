from django.http import HttpResponse

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from myrobot.models.models import MyRobot


@main_auth(on_cookies=True)
def uninstall(request):
    try:
        MyRobot.uninstall(request.bitrix_user_token)
    except Exception as exc:
        return HttpResponse(str(exc))

    return HttpResponse('ok')
