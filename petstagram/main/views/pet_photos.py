from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from petstagram.main.models import PetPhoto


class PetPhotoDetailsView(DetailView, LoginRequiredMixin):
    model = PetPhoto
    template_name = 'photos/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['is_owner'] = self.object.user == self.request.user
        return context

# LoginRequiredMixin => Loged in user required
class CreatePetPhotoView(LoginRequiredMixin, CreateView):
    model = PetPhoto
    template_name = 'photos/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets',)
    success_url = reverse_lazy('show dashboard')

    # the option to go to if you do not have a form beforehand
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(UpdateView):
    model = PetPhoto
    template_name = 'photos/photo_edit.html'
    fields = ('photo', 'description', 'tagged_pets')
    context_object_name = 'pet_photo'

    def get_success_url(self):
        return reverse_lazy('show pet photo details', kwargs={'pk': self.object.id})


class DeletePetPhotoView(DeleteView):
    model = PetPhoto
