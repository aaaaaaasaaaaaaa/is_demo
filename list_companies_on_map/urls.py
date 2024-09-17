from django.urls import path

from list_companies_on_map.views.views import list_companies_on_map
from list_companies_on_map.views.all_companies import companies

urlpatterns = [
    path('map/', list_companies_on_map, name="list_companies_on_map"),
    path('all_companies', companies)
]
