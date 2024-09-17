from django.shortcuts import render
from openpyxl.styles.builtins import title

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from collections import Counter
from ..forms import SelectForm


@main_auth(on_cookies=True)
def find_duplicates(request):
    category = ''
    check = ''
    but = request.bitrix_user_token
    lst = list()
    if request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            res = but.call_list_method(f'crm.{category}.list')
            if len(res) == 0:
                check = "Дубликатов не найдено."
            else:
                if category == 'deal':
                    name = "TITLE"
                else:
                    name = "NAME"
                for i in res:
                    lst.append(i[name])

    else:
        form = SelectForm()

    res = {name: count for name, count in Counter(lst).items() if count > 1}
    return render(request, 'duplicates.html', context={'res': res, 'form': form, 'title': category, 'check': check})
