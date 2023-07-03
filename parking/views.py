from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CarParkingAdministrator(LoginRequiredMixin, TemplateView):
    template_name = 'parking_spot_list.html'


class ExistingReservationsView(LoginRequiredMixin, TemplateView):
    template_name = 'existing_spot_list.html'

    # def get(self, request, *args, **kwargs):
    #     print(request.user)
    #     return super(CarParkingAdministrator, self).get(request, *args, **kwargs)
