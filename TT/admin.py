from django.contrib import admin
from .models import UserProfileModel, RoomMessages, Room

# Register your models here.
@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'dateOfBirth', 'picture']

admin.site.register(RoomMessages)
admin.site.register(Room)