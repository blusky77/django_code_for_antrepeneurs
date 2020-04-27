from django.urls import path
from products.views import product_detail_view, render_initial_data, dynamic_lookup_view, product_delete_view, \
    product_list_view

app_name = 'products'

urlpatterns = [
    # path('<int:id>', product_detail_view, name='product-detail'),
    path('create/', render_initial_data, name='create'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='delete'),
    path('', product_list_view, name='product-list'),
]
