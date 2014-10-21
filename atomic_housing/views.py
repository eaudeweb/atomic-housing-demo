from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.views.generic import UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
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
class LandLordListings(ListView):
    model = models.Listing
    template_name = 'landlord/listings.html'


class LandLordListingsAdd(CreateView):
    model = models.Listing
    form_class = forms.ListingForm
    success_url = reverse_lazy('listings')
    template_name = 'landlord/listings_edit.html'


class LandLordListingsEdit(UpdateView):
    model = models.Listing
    form_class = forms.ListingForm
    success_url = reverse_lazy('listings')
    template_name = 'landlord/listings_edit.html'


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


class MyFavorites(ListView):
    template_name = 'customer/favorites.html'
    model = models.Listing

    def get_queryset(self):
        try:
            return self.request.user.customer.favorites.all()
        except:
            return []


# Registration Views
class RegisterChoose(TemplateView):
    template_name = 'register/choose.html'


class RegisterCustomer(FormView):
    template_name = 'register/customer.html'
    form_class = forms.RegisterCustomerForm


class RegisterLandlord(FormView):
    template_name = 'register/landlord.html'
    form_class = forms.RegisterLandlordForm
