from django.urls import path
from .views import sort_fields


urlpatterns = [
    path('sort_fields/', sort_fields, name='sort_fields'),
]