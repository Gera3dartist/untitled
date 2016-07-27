Deploy guidelines

1) Install postgres server db(or any other and tweek settings)
2) create virtualenv: virtualenv --python=python3 (<3.5)
3) run: pip install -r requirements.txt
4) check the db settings in untitled.settings match with your local
5) run: ./manage.py migrate
6) run: ./manage.py loaddata deploy/initial.json
7) list api methods: ./manage.py show_urls
8) run server: ./manage.py runserver
9) Keep calm and send requests :)
10) Enjoy.


API Outline:

/wiki/pages/<pk>/       								wiki.views.WikiViewSet  wiki-manage:wikipage-detail
/wiki/pages/<pk>/update/        						wiki.views.WikiViewSet  wiki-manage:wikipage-update
/wiki/pages/<pk>/versions/      						wiki.views.WikiViewSet  wiki-manage:wikipage-versions
/wiki/pages/<pk>/versions/<version_id>/set_current/     wiki.views.WikiViewSet  wiki-manage:wikipage-versions/(?P<version-id>\d+)/set-current
/wiki/pages/create/     								wiki.views.WikiViewSet  wiki-manage:wikipage-create
/wiki/pages/list/									    wiki.views.WikiViewSet  wiki-manage:wikipage-list


TODO: Add Tests
plan:
    for function test: use Django native libs
    for end-to-end: django-behave

Time spent: ~ 7hours



