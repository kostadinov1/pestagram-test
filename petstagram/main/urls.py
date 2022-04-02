from django.urls import path

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pet_photos import CreatePetPhotoView, EditPetPhotoView, PetPhotoDetailsView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView, like_pet_photo

urlpatterns = [
    path('', HomeView.as_view(), name='show home'),
    path('dashboard/', DashboardView.as_view(), name='show dashboard'),


    path('pet/add/', CreatePetView.as_view(), name='show add pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='show edit pet'),
    path('pet/delete/<int:pk>', DeletePetView.as_view(), name='show delete pet'),

    path('photo/add/', CreatePetPhotoView.as_view(), name='show add photo'),
    path('photo/edit/<int:pk>', EditPetPhotoView.as_view(), name='show edit photo'),
    path('photo/details/<int:pk>', PetPhotoDetailsView.as_view(), name='show pet photo details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like pet photo'),
]