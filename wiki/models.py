from django.db import models

# Create your models here.


class WikiPage(models.Model):
    title = models.CharField(max_length=256, unique=True)
    text = models.TextField()
    is_current = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'wiki_page_table'
        app_label = 'wiki'
