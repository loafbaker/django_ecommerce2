from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from carts.mixins import TokenMixin
from .forms import AddressForm, UserAddressForm
from .mixins import UserCheckoutAPIMixin, LoginRequiredMixin, CartOrderMixin, UserCheckoutMixin
from .models import UserCheckout, UserAddress, Order
from .permissions import isOwnerAndAuth
from .serializers import OrderSerializer, OrderDetailSerializer, UserAddressSerializer


# API CBVs


class OrderListAPIView(ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [isOwnerAndAuth]
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        return Order.objects.filter(user_checkout__user=self.request.user)

class OrderRetrieveAPIView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [isOwnerAndAuth]
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

class UserCheckoutAPI(UserCheckoutAPIMixin, APIView):
    """
    Registered users need to authenticate before accessing the data,
    while non-registered users need to pass the user_checkout_token to access the data.
    N.B. User authenticate method is prior to the user checkout ID method
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        data = self.get_checkout_data(user=request.user)
        return Response(data)

    def post(self, request, format=None):
        email = request.data.get('email')
        data = self.get_checkout_data(user=request.user, email=email)
        return Response(data)

class UserAddressCreateAPIView(CreateAPIView):
    """
    The API view have no authentication to the user.
    """
    model = UserAddress
    serializer_class = UserAddressSerializer


class UserAddressListAPIView(TokenMixin, ListAPIView):
    """
    N.B. User authenticate method is prior to the user checkout ID method
    """
    authentication_classes = [SessionAuthentication]
    model = UserAddress
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    def get_queryset(self, *args, **kwargs):
        user_checkout_token = self.request.GET.get('user_checkout_token')
        try:
            user_checkout_data = self.parse_token(user_checkout_token)
            user_checkout_id = user_checkout_data.get('user_checkout_id')
        except:
            user_checkout_id = None
        if self.request.user.is_authenticated:
            return UserAddress.objects.filter(user_checkout__user=self.request.user)
        elif user_checkout_id:
            return UserAddress.objects.filter(user_checkout__id=int(user_checkout_id))
        else:
            return UserAddress.objects.none()

# CBVs

class AddressSelectFormView(CartOrderMixin, UserCheckoutMixin, FormView):
    form_class = AddressForm
    template_name = 'orders/address_select.html'

    def dispatch(self, *args, **kwargs):
        shipping_address, billing_address = self.get_addresses()
        if billing_address.count() == 0:
            messages.success(self.request, 'Please add a billing address before continuing.')
            return redirect('order_address_create')
        elif shipping_address.count() == 0:
            messages.success(self.request, 'Please add a shipping address before continuing.')
            return redirect('order_address_create')
        return super(AddressSelectFormView, self).dispatch(*args, **kwargs)

    def get_addresses(self, *args, **kwargs):
        user_checkout = self.get_user_checkout()
        if user_checkout is None:
            # Return empty UserAddress queryset
            return UserAddress.objects.none(), UserAddress.objects.none()
        address_queryset = UserAddress.objects.filter(user_checkout=user_checkout)
        billing_address = address_queryset.filter(type='billing')
        shipping_address = address_queryset.filter(type='shipping')
        return shipping_address, billing_address

    def get_form(self, *args, **kwargs):
        form = super(AddressSelectFormView, self).get_form(*args, **kwargs)
        shipping_address, billing_address = self.get_addresses()
        order = self.get_order()
        form.fields['billing_address'].queryset = billing_address
        form.fields['shipping_address'].queryset = shipping_address
        return form

    def form_valid(self, form, *args, **kwargs):
        shipping_address = form.cleaned_data['shipping_address']
        billing_address = form.cleaned_data['billing_address']
        order = self.get_order()
        order.shipping_address = shipping_address
        order.billing_address = billing_address
        order.save()
        return super(AddressSelectFormView, self).form_valid(form, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        return reverse('checkout:checkout')

class UserAddressCreateView(UserCheckoutMixin, CreateView):
    form_class = UserAddressForm
    template_name = 'forms.html'

    def form_valid(self, form, *args, **kwargs):
        user_checkout = self.get_user_checkout()
        if user_checkout is None:
            messages.success(self.request, 'Please confirm your identity before adding address.')
            return redirect('checkout')
        form.instance.user_checkout = user_checkout
        return super(UserAddressCreateView, self).form_valid(form, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        return reverse('checkout:order_address')

class OrderListView(LoginRequiredMixin, UserCheckoutMixin, ListView):
    queryset = Order.objects.all()

    def get_queryset(self):
        user_checkout = self.get_user_checkout()
        return super(OrderListView, self).get_queryset().filter(user_checkout=user_checkout)

class OrderDetailView(UserCheckoutMixin, DetailView):
    model = Order

    def dispatch(self, request, *args, **kwargs):
        user_checkout = self.get_user_checkout()
        obj = self.get_object()
        if user_checkout is not None and obj.user_checkout == user_checkout:
            return super(OrderDetailView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404
