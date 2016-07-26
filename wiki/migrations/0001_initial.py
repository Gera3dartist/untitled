# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            '''
CREATE TABLE wiki_page_table (
  id                         SERIAL PRIMARY KEY,
  title                 VARCHAR(128) UNIQUE,
  text                  TEXT,
  is_current                  BOOL DEFAULT FALSE                 NOT NULL,
  created                    TIMESTAMP WITH TIME ZONE           NOT NULL,
  updated                    TIMESTAMP WITH TIME ZONE           NOT NULL
);
            ''',
            '''
DROP TABLE wiki_page_table;
            ''',
            state_operations = [
                migrations.CreateModel(
                    name='WikiPage',
                    fields=[
                        ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                        ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                        ('updated', models.DateTimeField(auto_now=True)),
                        ('title', models.CharField(unique=True, max_length=256)),
                        ('text', models.TextField()),
                        ('is_current', models.BooleanField(default=False)),
                    ],
                    options={
                        'db_table': 'wiki_page_table',
                    },
                    bases=(models.Model,),
                ),
            ]
        )
    ]
