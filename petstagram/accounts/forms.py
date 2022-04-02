from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from petstagram.accounts.models import Profile
from petstagram.common.helpers import BootstrapFormMixin


# it should inherits UserCreationForm instead of ModeForm
class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LENGTH)
    last_name = forms.CharField(max_length=Profile.LAST_NAME_MAX_LENGTH)
    date_of_birth = forms.DateField()
    picture = forms.URLField()
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=Profile.GENDERS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                },

            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Last Name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            )
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                },

            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Last Name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs= {
                    'min': '1920-01-01'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'gender': forms.Select(
                    choices=Profile.GENDERS,

            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        #pets = list(self.instance.pet_set.all())
        #PetPhoto.objects.filter(tagged_pets=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
