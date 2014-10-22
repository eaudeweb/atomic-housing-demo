from django.core.urlresolvers import reverse_lazy
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.views.generic import UpdateView, DetailView, View

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


class LandLordListingsPhotosEdit(View):

    template_name = 'landlord/listings_photos.html'
    success_url = reverse_lazy('listings')

    def get(self, request, pk):
        listing = get_object_or_404(models.Listing, pk=pk)
        ListingPhotoFormSet = formset_factory(
            forms.ListingPhotoForm,
            formset=forms.BaseListingPhotoFormset,
            extra=1)
        formset = ListingPhotoFormSet()
        return render(request, self.template_name, {
            'listing': listing,
            'formset': formset,
        })

    def post(self, request, pk):
        listing = get_object_or_404(models.Listing, pk=pk)
        ListingPhotoFormSet = formset_factory(
            forms.ListingPhotoForm,
            formset=forms.BaseListingPhotoFormset,
            extra=1)
        formset = ListingPhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(listing)
            return redirect('listings_photos', pk=pk)
        return render(request, self.template_name, {
            'listing': listing,
            'formset': formset
        })


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
