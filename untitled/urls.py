"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from core.routers import CoreRouter
from django.conf.urls import url, include
from wiki.views import WikiViewSet

router = CoreRouter()


router.register(r'pages', WikiViewSet, base_name='wikipage')
urlpatterns = [
    url(r'^wiki/', include(router.urls, namespace='wiki-manage')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
