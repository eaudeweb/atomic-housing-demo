from django.conf.urls import patterns, include, url
from django.contrib import admin
from atomic_housing.views import *

urlpatterns = patterns('',

    url(r'hsadmin/', HSAdminHome.as_view(), name='hsadmin_home'),

    url(r'^admin/', include(admin.site.urls)),
)
