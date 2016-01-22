# -*- coding: Utf-8 -*-
from photos.models import *
from django.contrib import admin

class PhotosInline(admin.TabularInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ['nom']}
    
    fieldsets = [
        ('Propriété de l\'album', {'fields': ['nom', 'slug', 'date_album', 'texte', 'actif'], 'classes': ['wide']}),
    ]
    list_display = ('nom', 'date_album', 'actif')
    
    inlines = [PhotosInline,]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)