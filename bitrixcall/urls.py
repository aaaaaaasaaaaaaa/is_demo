from django.urls import path

from .views import bitrix_call

urlpatterns = [
    path('register_call/', bitrix_call, name='register_call'),
]
