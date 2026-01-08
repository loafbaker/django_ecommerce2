from django.urls import path

from orders.views import AddressSelectFormView, UserAddressCreateView
from .views import CheckoutView, CheckoutFinalView


app_name = 'checkout'

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('final/', CheckoutFinalView.as_view(), name='checkout_final'),
    path('address/', AddressSelectFormView.as_view(), name='order_address'),
    path('address/add/', UserAddressCreateView.as_view(), name='order_address_create'),
]