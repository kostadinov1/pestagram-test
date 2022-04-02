from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram.accounts.forms import CreateProfileForm, EditProfileForm
from petstagram.accounts.models import Profile
from petstagram.main.models import Pet, PetPhoto


class UserRegisterView(CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('show dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('show dashboard')
        return super().dispatch(request, *args, **kwargs)



class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    # this does not work without the method
    success_url = reverse_lazy('show dashboard')

    # this has to be added
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super(UserLoginView, self).get_success_url()


# def build_logout(request):
#     logout()


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Because the required classes (Pet and PetPhoto) are in another app it must be done with signals instead
        pets = list(Pet.objects.filter(user_id=self.object.user_id))
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context['total_likes_count'] = total_likes_count
        context['total_pet_photos_count'] = total_pet_photos_count
        context['is_owner'] = self.object.user.id == self.request.user.id
        context['pets'] = pets

        return context



class ProfileEditView(UpdateView):
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

class EditPasswordView(PasswordChangeView):
    success_url = reverse_lazy('show profile details')



