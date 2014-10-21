from django.views.generic import TemplateView, ListView
from atomic_housing.models import Listing

# HS Admin Views
class HSAdminHome(TemplateView):
    template_name = 'hsadmin/home.html'


class HSAdminListings(ListView):
    template_name = 'hsadmin/listing_list.html'
    model = Listing


# Landlord Views


# Customer Views
