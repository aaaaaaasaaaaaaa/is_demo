from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from allcompbizproc.forms.select_bp import BPForm
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth

from allcompbizproc.models.bizprocmodel import BizprocModel


@main_auth(on_cookies=True)
def run_bizproc(request):
    but = request.bitrix_user_token
    lead_id = but.call_list_method('crm.lead.list', {'select': ['ID']})
    BizprocModel.find_all_bizprocs(but)
    counter = len(lead_id)
    if request.method == 'POST':
        form = BPForm(request.POST)
        if form.is_valid():
            cur_bp = form.cleaned_data['bp']
            for company in lead_id:
                cur_bp.run_cur_bizproc(but, company['ID'])
            return render(request, 'allcompbizproc.html', context={'form': form, 'counter': counter})
    else:
        form = BPForm()
    return render(request, 'allcompbizproc.html', context={'form': form})