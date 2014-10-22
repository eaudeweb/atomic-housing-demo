from django.forms import ModelForm, BaseFormSet
from django.forms.models import BaseModelFormSet
from atomic_housing import models
from atomic_housing.middleware import get_current_request


class ListingForm(ModelForm):

    class Meta:
        model = models.Listing
        exclude = ('owner', 'status', 'posted',)

    def save(self):
        listing = super(ListingForm, self).save(commit=False)
        request = get_current_request()
        listing.owner = request.user
        listing.save()
        return listing


class RegisterCustomerForm(ModelForm):

    class Meta:
        model = models.Customer


class RegisterLandlordForm(ModelForm):

    class Meta:
        model = models.Landlord


class ListingPhotoForm(ModelForm):

    class Meta:
        model = models.ListingPhoto
        exclude = ('listing',)

    def save(self, listing):
        photo = super(ListingPhotoForm, self).save(commit=False)
        photo.listing = listing
        photo.save()


class BaseListingPhotoFormset(BaseFormSet):

    def save(self, listing):
        for form in self.forms:
            if not form.cleaned_data:
                continue
            form.save(listing=listing)
