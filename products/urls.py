from django.urls import path

from .views import ProductDetailView, ProductListView, VariationListView, product_detail_view_func


app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/inventory/', VariationListView.as_view(), name='product_inventory'),
    # path('<int:id>/', product_detail_view_func, name='product_detail'),
]