from django_filters import FilterSet, CharFilter, NumberFilter

from .models import Product

# Filter Class

class ProductFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    category = CharFilter(field_name='categories__title', lookup_expr='icontains', distinct=True)
    category_id = CharFilter(field_name='categories__id', lookup_expr='iexact', distinct=True)
    min_price = NumberFilter(field_name='variation__price', lookup_expr='gte', distinct=True)
    max_price = NumberFilter(field_name='variation__price', lookup_expr='lte', distinct=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'category',
            'min_price',
            'max_price',
        ]
