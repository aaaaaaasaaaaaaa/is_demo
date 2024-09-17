from django.shortcuts import redirect
from django.urls import reverse
from settings import DOMAIN
from django.http import Http404
from ..utils.is_handler_bound import is_bound
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def unbind_button(request):
    """Отвязываем хендлер от окна просмотра задачи"""
    if request.method != "POST":
        raise Http404()

    handler_type = request.GET.get("type")

    if request.bitrix_user.is_admin and handler_type in ["js", "server", "admin", "auth", "self"]:
        if is_bound(request.bitrix_user_token, handler_type):
            request.bitrix_user_token.call_api_method("placement.unbind", params={
                "PLACEMENT": "TASK_VIEW_SIDEBAR",
                "HANDLER": DOMAIN + reverse('move_tasks_deadline_js:move_button') + "?type=" + handler_type
            })

    return redirect(reverse("move_tasks_deadline_js:index"))
