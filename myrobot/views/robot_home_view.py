from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from myrobot.models.models import MyRobot


@main_auth(on_cookies=True)
def robot_home(request):

    return render(request, 'my_robot.html', locals())
