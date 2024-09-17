from django.urls import path

from .views.excel_products_pandas import product_in_excel


urlpatterns = [
    path('product_excel_pandas/', product_in_excel, name='product_in_excel'),
]
