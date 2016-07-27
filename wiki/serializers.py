from django.db import transaction
from rest_framework import serializers
from wiki.models import WikiPage, WikiPageVersions

__author__ = 'agerasym'

class BadArgumentsException(Exception):
    pass

class BaseFieldValidator(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        data = kwargs.get('data', {})
        for key in data.keys():
            if key not in self.Meta.fields:
                raise BadArgumentsException('bad args')
        super().__init__(*args, **kwargs)


class WikiPageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiPage
        exclude = ['text']


class WikiPageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiPage


class WikiPageCreateUpdateBase(serializers.ModelSerializer):
    class Meta:
        model = WikiPage
        fields = ('title', 'text')

    def record_version(self, instance):
        WikiPageVersions.objects.create(**{
            'title': instance.title,
            'text': instance.text,
            'is_current': True,
            'page': instance
        })


class WikiPageCreateSerializer(WikiPageCreateUpdateBase):
    class Meta(WikiPageCreateUpdateBase.Meta):
        pass

    def create(self, validated_data):
        instance = super().create(validated_data)

        # hack to enable pycharm's autocomplete
        assert isinstance(instance, WikiPage)
        # make version record
        self.record_version(instance)
        return instance


class WikiPageUpdateSerializer(WikiPageCreateUpdateBase):
    class Meta(WikiPageCreateUpdateBase.Meta):
        pass

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # hack to enable pycharm's autocomplete
        assert isinstance(instance, WikiPage)

        # update history state
        instance.versions.clear_current()
        # make version record
        self.record_version(instance)
        return instance

class WikiPageUpdateVersionSerializer(WikiPageCreateUpdateBase):

    def __init__(self, *args, **kwargs):
        self.version = kwargs.pop('version', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = WikiPage
        fields = []
        # fields = ('title', 'text')

    def validate(self, attrs):
        self.version = self.instance.versions.filter(id=self.version).first()
        if not self.version:
            raise serializers.ObjectDoesNotExist('wrong version id')
        return super().validate(attrs)

    @transaction.atomic
    def update(self, instance, validated_data):
        # update current version
        instance.versions.set_current(version_id=self.version.id)

        # update instance
        validated_data['text'] = self.version.text
        validated_data['title'] = self.version.title
        return super().update(instance, validated_data)


class WikiPageVersionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiPageVersions
        fields = ('id', 'is_current', 'created')
