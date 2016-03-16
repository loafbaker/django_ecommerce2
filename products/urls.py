from django.conf.urls import url

from .views import ProductDetailView, ProductListView, VariationListView, product_detail_view_func


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    #url(r'^(?P<id>\d+)/$', product_detail_view_func, name='product_detail'),
]