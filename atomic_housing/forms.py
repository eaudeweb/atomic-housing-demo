from django.forms import ModelForm
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
