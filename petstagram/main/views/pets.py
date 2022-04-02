from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from petstagram.main.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main.models import PetPhoto, Pet


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo_details.html', pk)


class CreatePetView(CreateView):
    model = Pet
    template_name = 'pets/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('show dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(UpdateView):
    model = Pet
    template_name = 'pets/pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('show dashboard')


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet_delete.html'
    success_url = reverse_lazy('show dashboard')
    #form_class = DeletePetForm

