from django.contrib import admin

from petstagram.accounts.models import PetstagramUser, Profile


@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass



