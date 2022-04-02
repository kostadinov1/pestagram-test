from django import forms
from petstagram.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from petstagram.main.models import Pet, PetPhoto


YEARS_CHOICES = range(1920, 2022)


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false modify it so does not persist to database
        # just returns the object to be created
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Pet Name',
                },
            ),
            'type': forms.Select(
                choices=Pet.TYPES
            ),
            'date_of_birth': forms.SelectDateWidget(
               years=YEARS_CHOICES
            )
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Pet Name',
                },
            ),
            'type': forms.Select(
                choices=Pet.TYPES
            ),
            'date_of_birth': forms.SelectDateWidget(
                years=YEARS_CHOICES
            )
        }


class DeletePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)


# class DeletePetForm(BootstrapFormMixin, forms.ModelForm, DisabledFieldsFormMixin):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#         self._init_disabled_fields()
#
#     def save(self, commit=True):
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Pet
#         fields = ('name', 'type', 'date_of_birth')
#         exclude = ('user_profile',)
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={
#                     'editable': False,
#                 },
#
#             ),
#             'type': forms.Select(
#                 choices=Pet.TYPES,
#                 attrs={
#                     'readonly': 'readonly',
#                 },
#             ),
#             'date_of_birth': forms.SelectDateWidget(
#                 years=YEARS_CHOICES,
#                 attrs={
#                     'disabled': True,
#                 },
#             )
#         }


class CreatePetPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'
