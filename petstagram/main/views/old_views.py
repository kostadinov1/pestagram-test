

#   ALL THIS NEEDS TO BE COMMMENTED FOR THE PROJECT TO WORK

#
# def show_pet_photo_details(request, pk):
#     pet_photo = PetPhoto.objects.get(pk=pk)
#     context = {
#         'pet_photo': pet_photo,
#     }
#     return render(request, 'photos/photo_details.html', context)
#
#
# def add_photo(request):
#
#     return render(request, 'photos/photo_create.html')
#
#
# def edit_photo(request):
#
#     return render(request, 'photos/photo_create.html')
#
#
#
# def add_pet(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = CreatePetForm(request.POST, instance=Pet(user_profile=profile))
#         if form.is_valid():
#             form.save()
#             return redirect('show profile details')
#
#     form = CreatePetForm(instance=Pet(user_profile=profile))
#
#     context = {
#         'form': form
#     }
#     return render(request, 'pets/pet_create.html', context)
#
#
# def edit_pet(request, pk):
#     this_instance = Pet.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EditPetForm(request.POST, instance=this_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('show profile details')
#
#     form = EditPetForm(instance=this_instance)
#
#     context = {
#         'form': form,
#         'pk': pk,
#         'instance': this_instance
#     }
#     return render(request, 'pets/pet_edit.html', context)
#
#
# def delete_pet(request, pk):
#
#     this_instance = Pet.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = DeletePetForm(request.POST, instance=this_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('show profile details')
#
#     form = DeletePetForm(instance=this_instance)
#
#     context = {
#         'form': form,
#         'pk': pk,
#         'instance': this_instance
#     }
#     return render(request, 'pets/pet_delete.html', context)
