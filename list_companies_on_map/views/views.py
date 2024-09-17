from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def list_companies_on_map(request):
    but = request.bitrix_user_token
    comp_id = but.call_list_method('crm.company.list')
    address = but.call_list_method('crm.address.list')
    return render(request, 'show_companies_on_map.html', locals())
