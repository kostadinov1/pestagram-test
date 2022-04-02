from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.accounts.managers import PetstagramUserManager
from petstagram.common.validators import validate_only_letters


class PetstagramUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    objects = PetstagramUserManager()
    USERNAME_FIELD = 'username'




class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    date_of_birth = models.DateField(null=True,blank=True,)
    picture = models.URLField()
    description = models.TextField(null=True,blank=True,)
    email = models.EmailField(null=True,blank=True,)
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(PetstagramUser, on_delete=models.CASCADE, primary_key=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
