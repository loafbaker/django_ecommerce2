from rest_framework.pagination import LimitOffsetPagination

class ProductPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'


class CategoryPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'