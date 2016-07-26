from rest_framework import viewsets

from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from wiki.models import WikiPage
from wiki.serializers import WikiPageSerializer, \
    WikiPageDetailSerializer, WikiPageCreateSerializer
from rest_framework.decorators import detail_route, list_route

__author__ = 'agerasymchuk'


class WikiViewSet(viewsets.ModelViewSet):
    model = WikiPage
    queryset = WikiPage.objects.all()
    serializer_class = WikiPageSerializer
    paginate_by = 25

