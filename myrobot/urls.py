from django.urls import path

from .models.models import MyRobot
from .views.install import install
from .views.robot_home_view import robot_home
from .views.uninstall import uninstall

app_name = 'my_robot'

urlpatterns = [
    path('home/', robot_home, name='robot_home'),
    path('install/', install, name='install_robot'),
    path('uninstall/', uninstall, name='uninstall_robot'),
    path('handler/', MyRobot.as_view(), name='handler_robot'),
]
