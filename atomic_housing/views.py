from django.views.generic import TemplateView


class HSAdminHome(TemplateView):
    template_name = 'hsadmin/home.html'
