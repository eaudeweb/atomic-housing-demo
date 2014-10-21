from django.conf.urls import patterns, include, url
from django.contrib import admin
from atomic_housing.views import *

urlpatterns = patterns('',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^hsadmin/$', HSAdminHome.as_view(), name='hsadmin_home'),
    url(r'^hsadmin/landlord/list', HSAdminLandlords.as_view(),
        name='hsadmin_landlord_list'),
    url(r'^hsadmin/customer/list', HSAdminCustomers.as_view(),
        name='hsadmin_customer_list'),
    url(r'^hsadmin/listing/list', HSAdminListings.as_view(),
        name='hsadmin_listing_list'),
    url(r'^hsadmin/contract/list', HSAdminContracts.as_view(),
        name='hsadmin_contract_list'),

    url(r'^landlord/listings/add', LandLordListingsAdd.as_view(),
        name='listing_add'),

    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^detail/(?P<pk>\d+)/$', ListingDetails.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
