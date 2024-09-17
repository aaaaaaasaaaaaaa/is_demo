from django.urls import path

from load_companies_to_bd.views.views import load_companies_to_bd

urlpatterns = [
    path('load_companies', load_companies_to_bd, name="load_companies_to_bd"),
]
