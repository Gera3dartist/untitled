from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

__author__ = 'agerasym'


class ModelViewGetter(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    http_method_names = ['post', 'get']

    def list_or(self, request, qs, *args, **kwargs):
        query = self.filter_queryset(qs)
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)