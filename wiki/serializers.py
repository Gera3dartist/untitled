from rest_framework import serializers
from wiki.models import WikiPage

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

class WikiPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = WikiPage
        exclude = ['text']


class WikiPageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiPage


class WikiPageCreateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['is_current'] = True
        return attrs

    class Meta:
        model = WikiPage
        fields = ('fields', 'title', 'text')
