from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

__author__ = 'agerasym'


class ModelViewGetter(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    pass