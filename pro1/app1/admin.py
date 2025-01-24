from django.contrib import admin
from .models import Image, Blog, Scooter

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    
@admin.register(Scooter)
class ScooterAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')