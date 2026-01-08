"""
URL configuration for django_ecommerce2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from newsletter import views as newsletter_views
from . import views as main_views


from carts.views import (
        CartAPIView,
        CheckoutAPIView,
        CheckoutFinalizeAPIView,
    )

from orders.views import (
        OrderListAPIView,
        OrderRetrieveAPIView,
        UserCheckoutAPI,
        UserAddressCreateAPIView,
        UserAddressListAPIView,
    )

from products.views import (
        APIHomeView,
        ProductListAPIView,
        ProductRetrieveAPIView,
        CategoryListAPIView,
        CategoryRetrieveAPIView,
    )

urlpatterns = [
    path('', newsletter_views.home, name='home'),
    path('contact/', newsletter_views.contact, name='contact'),
    path('about/', main_views.about, name='about'),
    path('cart/', include('carts.urls', namespace='carts')),
    path('checkout/', include('carts.urls_checkout', namespace='checkout')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('products/', include('products.urls', namespace='products')),
    path('categories/', include('products.urls_categories', namespace='categories')),

    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
]

urlpatterns += [
    path('api/', APIHomeView.as_view(), name='home_api'),
    path('api/cart/', CartAPIView.as_view(), name='cart_api'),
    path('api/checkout/', CheckoutAPIView.as_view(), name='checkout_api'),
    path('api/checkout/finalize/', CheckoutFinalizeAPIView.as_view(), name='checkout_finalize_api'),
    path('api/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='auth_login_api'),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token_api'),
    path('api/user/checkout/', UserCheckoutAPI.as_view(), name='user_checkout_api'),
    path('api/user/address/', UserAddressListAPIView.as_view(), name='user_address_list_api'),
    path('api/user/address/create/', UserAddressCreateAPIView.as_view(), name='user_address_create_api'),
    path('api/orders/', OrderListAPIView.as_view(), name='orders_api'),
    path('api/orders/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order_detail_api'),
    path('api/products/', ProductListAPIView.as_view(), name='products_api'),
    path('api/products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail_api'),
    path('api/categories/', CategoryListAPIView.as_view(), name='categories_api'),
    path('api/categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
