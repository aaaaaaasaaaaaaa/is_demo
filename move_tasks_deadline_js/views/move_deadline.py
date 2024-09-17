from django.shortcuts import render
from django.http import Http404, HttpResponse
from torch.fx.experimental.unification.unification_tools import first

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from integration_utils.bitrix24.models.bitrix_user import BitrixUser
from datetime import datetime, timedelta


@main_auth(on_cookies=True)
def move_deadline(request):
    """Сдвигает крайний срок задачи на день по токену админа"""
    if request.method != "POST":
        raise Http404()

    button_type = request.GET.get("type")

    if button_type not in ["server", "admin", "auth", "self"]:
        raise Http404()

    resp = render(request, 'move_tasks_deadline_js/move_button.html', {
        "button_type": button_type,
        "path_to_script": "move_tasks_deadline_js/admin.js"
    })

    task_id = request.POST.get("task_id")

    if not task_id:
        return resp

    if button_type == "server":
        but = BitrixUser.objects.first().bitrix_user_token


    if button_type == "admin":
        but = BitrixUser.objects.filter(is_admin=True, user_is_active=True).first().bitrix_user_token

    if button_type == "auth":
        but = BitrixUser.objects.filter(is_admin=True, user_is_active=True).first().bitrix_user_token

    if button_type == "self":
        but = request.bitrix_user_token
        response = but.call_api_method("tasks.task.get", params={
            "taskId": task_id,
            "select": ["DEADLINE", "CREATED_BY"]
        })

        id_user = request.bitrix_user.bitrix_id
        print(int(response["result"]["task"]["createdBy"]), id_user)
        if int(response["result"]["task"]["createdBy"]) != id_user:
            return HttpResponse("Ошибка.")

    response = but.call_api_method("tasks.task.get", params={
        "taskId": task_id,
        "select": ["DEADLINE", "CREATED_BY"]
    })
    deadline_iso = response["result"]["task"]["deadline"]

    if not deadline_iso:
        return resp

    deadline = datetime.fromisoformat(deadline_iso)
    deadline += timedelta(days=1)
    deadline_iso = deadline.isoformat()

    but.call_api_method("tasks.task.update", params={
        "taskId": task_id,
        "fields": {"DEADLINE": deadline_iso}
    })

    return resp
