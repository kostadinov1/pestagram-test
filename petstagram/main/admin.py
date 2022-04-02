from django.contrib import admin

from petstagram.main.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
    list_display = ('id','likes')

