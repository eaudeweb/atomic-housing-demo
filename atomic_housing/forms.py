from django.forms import ModelForm
from atomic_housing import models


class ListingForm(ModelForm):

    class Meta:
        model = models.Listing
        exclude = ('owner', 'status', 'posted',)

    def save(self):
        listing = super(ListingForm, self).save(commit=False)
        listing.save()
        return listing
