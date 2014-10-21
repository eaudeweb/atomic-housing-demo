from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from atomic_housing import models, forms


# HS Admin Views
class HSAdminHome(TemplateView):

    template_name = 'hsadmin/home.html'


class HSAdminListings(ListView):
    template_name = 'hsadmin/listing_list.html'
    model = models.Listing


class HSAdminLandlords(ListView):
    template_name = 'hsadmin/landlord_list.html'
    model = models.Landlord


class HSAdminCustomers(ListView):
    template_name = 'hsadmin/customer_list.html'
    model = models.Customer


# Landlord Views
class LandLordListingsAdd(CreateView):

    model = models.Listing
    form_class = forms.ListingForm
    template_name = 'landlord/listing_edit.html'


class LandLordListingEdit(UpdateView):

    model = models.Listing
    form_class = forms.ListingForm
    template_name = 'landlord/listing_edit.html'


# Customer Views
