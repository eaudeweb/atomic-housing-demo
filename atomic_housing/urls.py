from django.conf.urls import patterns, include, url
from django.contrib import admin
from atomic_housing.views import *

urlpatterns = patterns('',
    url(r'^hsadmin/$', HSAdminHome.as_view(), name='hsadmin_home'),
    url(r'^hsadmin/listing/list', HSAdminListings.as_view(),
        name='hsadmin_listing_list'),

    url(r'^admin/', include(admin.site.urls)),
)
