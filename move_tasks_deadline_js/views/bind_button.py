from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import Http404
from ..utils.is_handler_bound import is_bound
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def bind_button(request):
    """Привязываем хендлер к окну просмотра задачи"""
    if request.method != "POST":
        raise Http404()

    print('1')

    handler_type = request.GET.get("type")
    print('2')

    if request.bitrix_user.is_admin and handler_type in ["js", "server", "admin", "auth", "self"]:
        print('3')
        if not is_bound(request.bitrix_user_token, handler_type):
            print('4')
            request.bitrix_user_token.call_api_method("placement.bind", params={
                "PLACEMENT": "TASK_VIEW_SIDEBAR",
                "HANDLER": settings.DOMAIN + reverse('move_tasks_deadline_js:move_button') + "?type=" + handler_type
            })
            print('6')
    print('5')
    return redirect(reverse("move_tasks_deadline_js:index"))
