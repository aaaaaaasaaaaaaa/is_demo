from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
import json


@main_auth(on_cookies=True)
def company_fields_list(request):
    but = request.bitrix_user_token
    res = but.call_list_method("crm.company.list")
    all_companies = []

    for company in res:
        data = {
            "ID": company.get("ID", 'None'),
            "TITLE": company.get("TITLE", 'None'),
            "DATE": company.get("DATE_CREATE", 'None'),
            "ADDRESS": company.get("ADDRESS", 'None'),
            'ADDRESS_CITY': company.get("ADDRESS_CITY", 'None'),
        }
        all_companies.append(data)

    all_companies = json.dumps(all_companies)

    return render(request, 'showcompanyfields.html', context={'all_companies': all_companies})
