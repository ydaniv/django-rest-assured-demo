from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()


# this shall serve as our urls auto-discovery
from drademo.blog.urls import register
register(router)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
