from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from .forms import MyCallInfoForm



@main_auth(on_cookies=True)
def bitrix_call(request):
    but = request.bitrix_user_token
    if request.method == 'POST':
        form = MyCallInfoForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save()
            model.telephony_externalcall_register(but)
            model.telephony_externalcall_finish(but)
    form = MyCallInfoForm()
    return render(request, 'myregistercall.html', locals())