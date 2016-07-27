# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            '''
CREATE TABLE wiki_page_storage (
  id                         serial PRIMARY KEY,
  title                 VARCHAR(128),
  text                  TEXT,
  is_current                  BOOL DEFAULT FALSE                 NOT NULL,
  created                    TIMESTAMP WITH TIME ZONE           NOT NULL,
  updated                    TIMESTAMP WITH TIME ZONE           NOT NULL
);

CREATE TABLE wiki_page_versions (
  id                         bigserial PRIMARY KEY,
  page_id INTEGER REFERENCES wiki_page_storage(id),
  title                 VARCHAR(128),
  text                  TEXT,
  is_current                  BOOL DEFAULT FALSE                 NOT NULL,
  created                    TIMESTAMP WITH TIME ZONE           NOT NULL
);
            ''',
            '''
DROP TABLE wiki_page_storage;
DROP TABLE wiki_page_versions;
            ''',
            state_operations = [
                migrations.CreateModel(
                    name='WikiPage',
                    fields=[
                        ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                        ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                        ('updated', models.DateTimeField(auto_now=True)),
                        ('title', models.CharField(max_length=256)),
                        ('text', models.TextField()),
                    ],
                    options={
                        'db_table': 'wiki_page_storage',
                    },
                    bases=(models.Model,),
                ),
                migrations.CreateModel(
                    name='WikiPageVersions',
                    fields=[
                        ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                        ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                        ('title', models.CharField(max_length=256)),
                        ('text', models.TextField()),
                        ('is_current', models.BooleanField(default=False)),
                    ],
                    options={
                        'db_table': 'wiki_page_versions',
                    },
                    bases=(models.Model,),
                ),
            ]
        )
    ]
