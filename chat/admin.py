from django.contrib import admin
from .models import Room, Post


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
