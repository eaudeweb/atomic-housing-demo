from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic import UpdateView, DetailView
from atomic_housing import models, forms


class Homepage(TemplateView):
    template_name = 'homepage.html'


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


class HSAdminContracts(ListView):
    template_name = 'hsadmin/contract_list.html'
    model = models.Contract


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
class SearchView(ListView):
    template_name = 'customer/search.html'
    model = models.Listing

    def get_queryset(self):
        print self.request
        return super(SearchView, self).get_queryset()


class ListingDetails(DetailView):
    template_name = 'customer/detail.html'
    model = models.Listing
