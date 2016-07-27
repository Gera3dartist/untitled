
from rest_framework.response import Response
from wiki.base_view import ModelViewGetter
from wiki.models import WikiPage
from wiki.serializers import WikiPageDetailSerializer, \
    WikiPageCreateSerializer, WikiPageUpdateSerializer, \
    WikiPageUpdateVersionSerializer, \
    WikiPageVersionsListSerializer, WikiPageListSerializer
from rest_framework.decorators import detail_route, list_route

__author__ = 'agerasymchuk'


class WikiViewSet(ModelViewGetter):
    methods = ['GET', 'POST']
    model = WikiPage
    queryset = WikiPage.objects.all()
    serializer_class = WikiPageListSerializer
    paginate_by = 25

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = WikiPageDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    @list_route(methods=['post'], serializer_class=WikiPageCreateSerializer)
    def create(self, request , *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 200, 'data': {'id': serializer.instance.id}})

    @detail_route(methods=['post'], serializer_class=WikiPageUpdateSerializer)
    def update(self, request , pk, *args, **kwargs):
        wikipage = self.get_object()
        serializer = self.serializer_class(instance=wikipage, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 200})

    @detail_route(methods=['get'],
                  serializer_class=WikiPageVersionsListSerializer,
                  url_path='versions')
    def versions_list(self, request, pk, *args, **kwargs):
        wikipage = self.get_object()
        assert isinstance(wikipage, WikiPage)
        version_query = wikipage.versions.get_versions_list()

        current = request.GET.get('is_current', False)
        if current:
            version_query = version_query.get_current()

        return self.list_or(request, version_query,*args, **kwargs)

    @detail_route(methods=['post'],
                  serializer_class=WikiPageUpdateVersionSerializer,
                  url_path='versions/(?P<version_id>\d+)/set_current')
    def set_version(self, request, pk, version_id, *args, **kwargs):
        wikipage = self.get_object()
        serializer = self.serializer_class(
            instance=wikipage, version=version_id, data={})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 200})

