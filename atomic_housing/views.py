from django.views.generic import TemplateView, ListView
from atomic_housing.models import *

# HS Admin Views
class HSAdminHome(TemplateView):
    template_name = 'hsadmin/home.html'


class HSAdminListings(ListView):
    template_name = 'hsadmin/listing_list.html'
    model = Listing


class HSAdminLandlords(ListView):
    template_name = 'hsadmin/landlord_list.html'
    model = Landlord


class HSAdminCustomers(ListView):
    template_name = 'hsadmin/customer_list.html'
    model = Customer


# Landlord Views


# Customer Views
