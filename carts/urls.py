from django.urls import path

from .views import CartView, ItemCountView


app_name = 'carts'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('count/', ItemCountView.as_view(), name='cartitem_count'),
]