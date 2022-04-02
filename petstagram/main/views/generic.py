from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from petstagram.main.models import PetPhoto


class HomeView(TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('show dashboard')

        return super().dispatch(request, *args, **kwargs)


class DashboardView(ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'



