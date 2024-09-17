from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth

from load_companies_to_bd.models.models import Company

@main_auth(on_cookies=True)
def load_companies_to_bd(request):
    but = request.bitrix_user_token
    comment = ''

    if request.method == 'POST':
        Company.sync_companies(but)
        comment = 'БД обновлена'

    return render(request, 'load_companies.html', {comment: 'comment'})




