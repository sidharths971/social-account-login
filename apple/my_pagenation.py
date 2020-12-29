from  rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class my_pagenation(PageNumberPagination):
    page_size = 1
    page_query_param = 'p'

class my_limit_offset(LimitOffsetPagination):
    default_limit = 2
    offset_query_description = 'qsd'

class my_curser_pagenation(CursorPagination):
    page_size = 3
    ordering = 'name'
