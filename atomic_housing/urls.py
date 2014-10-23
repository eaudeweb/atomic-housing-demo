from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from atomic_housing import views
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.Homepage.as_view(), name='homepage'),

    url(r'^hsadmin/$', views.HSAdminHome.as_view(), name='hsadmin_home'),
    url(r'^hsadmin/landlord/list', views.HSAdminLandlords.as_view(),
        name='hsadmin_landlord_list'),
    url(r'^hsadmin/customer/list', views.HSAdminCustomers.as_view(),
        name='hsadmin_customer_list'),
    url(r'^hsadmin/listing/list', views.HSAdminListings.as_view(),
        name='hsadmin_listing_list'),
    url(r'^hsadmin/contract/list', views.HSAdminContracts.as_view(),
        name='hsadmin_contract_list'),

    url(r'^landlord/listings$',
        login_required(views.LandLordListings.as_view()),
        name='listings'),
    url(r'^landlord/listings/add$',
        login_required(views.LandLordListingsAdd.as_view()),
        name='listings_add'),
    url(r'^landlord/listings/(?P<pk>.*)/edit$',
        login_required(views.LandLordListingsEdit.as_view()),
        name='listings_edit'),
    url(r'^landlord/listings/(?P<pk>.*)/photos$',
        login_required(views.LandLordListingsPhotosEdit.as_view()),
        name='listings_photos'),
    url(r'^landlord/listings/(?P<pk>.*)/photos/(?P<photo_pk>.*)/delete$',
        login_required(views.LandLordListingsPhotoDelete.as_view()),
        name='listings_photos_delete'),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^register/choose/$', views.RegisterChoose.as_view(),
        name='register'),
    url(r'^register/customer/$', views.RegisterCustomer.as_view(),
        name='register_customer'),
    url(r'^register/landlord/terms$', views.RegisterLandlordTerms.as_view(),
        name='register_landlord_terms'),
    url(r'^register/landlord$', views.RegisterLandlord.as_view(),
        name='register_landlord'),


    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^detail/(?P<pk>\d+)/$', views.ListingDetails.as_view(),
        name='detail'),
    url(r'^favorites/$', views.MyFavorites.as_view(), name='favorites'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
