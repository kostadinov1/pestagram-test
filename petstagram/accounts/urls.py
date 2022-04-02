from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import UserRegisterView, UserLoginView, ProfileDetailsView, ProfileEditView, \
    EditPasswordView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='show register'),
    path('login/', UserLoginView.as_view(), name='show login'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='show profile details'),
    path('edit-profile/', ProfileEditView.as_view(), name='show edit profile'),
    path('edit-password/', EditPasswordView.as_view(), name='show change password'),
    path('password-changed/', RedirectView.as_view(url=reverse_lazy('show dashboard')), name='show password changed'),

)