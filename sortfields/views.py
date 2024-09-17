from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
import locale



@main_auth(on_cookies=True)
def sort_fields(request):
    if request.method == 'POST':
        but = request.bitrix_user_token
        res = but.call_list_method('crm.company.userfield.list', {'FILTER': {'FIELD_NAME': 'UF_CRM_1724755165'}})[0]
        field_id = res['ID']
        comp_list = res['LIST']
        def sort_companies_by_name(company_list):
            locale.setlocale(locale.LC_ALL, '')

            def sort_key(item):
                return locale.strxfrm(item['VALUE'])

            sorted_companies = sorted(company_list, key=sort_key)
            for index, company in enumerate(sorted_companies):
                company['SORT'] = index + 1
            return sorted_companies

        sorted_data = sort_companies_by_name(comp_list)

        but.call_list_method('crm.company.userfield.update', {'ID': field_id, 'FIELDS': {'LIST': sorted_data}})
        return render(request, 'sort_list.html', context={'count': len(sorted_data)})

    return render(request, 'sort_list.html')
