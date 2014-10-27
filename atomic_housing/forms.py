from django.forms import ModelForm, BaseFormSet, Form, ChoiceField, CharField
from django.forms.models import BaseModelFormSet
from atomic_housing import models
from atomic_housing.middleware import get_current_request
from django import forms


SORTBY_CHOICES = (
    ('rent', 'Price (ascending)'),
    ('-rent', 'Price (descending)'),
    ('updated', 'Date Posted'),
    ('size', 'Size (ascending)'),
    ('-size', 'Size (descending)'),
)


class ListingForm(ModelForm):
    class Meta:
        model = models.Listing
        exclude = ('owner', 'status', 'posted',)

    accomodation = forms.ChoiceField(choices=models.ACCOMODATION_TYPES,
                                     widget=forms.RadioSelect)

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
        exclude = ('user',)


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


class SearchForm(Form):
    search = CharField()
    sortby = ChoiceField(choices=SORTBY_CHOICES)
