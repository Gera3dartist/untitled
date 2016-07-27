from django.db import models

# Create your models here.
from wiki.managers import WikiPagesManager, WikiPagesVersionManager

_app_label = 'wiki'


class WikiPage(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    objects = WikiPagesManager()

    class Meta:
        db_table = 'wiki_page_storage'
        app_label = _app_label


class WikiPageVersions(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    is_current = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    page = models.ForeignKey('WikiPage', related_name='versions')

    objects = WikiPagesVersionManager()

    class Meta:
        db_table = 'wiki_page_versions'
        app_label = _app_label
