# -*- encoding: utf-8 -*-
from appels.models import *
from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

class Appel_OffreAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ['titre']}
    fieldsets = [
        ('Article', {'fields': ['status', 'titre', 'slug', 'image', 'resume', 'texte'], 'classes': ['wide']}),
        ('Date', {'fields': ['date_fin', 'date_fin2'], 'classes': ['wide']}),
    ]

    #formfield_overrides = {
        #models.TextField: {'widget': TinyMCE(attrs={'cols': 60, 'rows': 24}, )},
    #}

    def show_image(self, obj):
      return "<img src='../../../media/%s' style='height:90px;'>" % obj.image
    show_image.allow_tags = True #permet de sortir du html#
    show_image.short_description = 'Image'

    list_display = ('status','show_image',  'titre', 'date_pub')
    list_display_links = ('status', 'titre')
    search_fields = ['titre']


admin.site.register(Appel_Offre, Appel_OffreAdmin)
