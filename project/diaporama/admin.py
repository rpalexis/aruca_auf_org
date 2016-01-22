# -*- encoding: utf-8 -*-
from project.diaporama.models import Slider
from django.contrib import admin
from django.db import models

class SliderAdmin(admin.ModelAdmin):
    
        
    def show_image(self, obj):
      return "<img src='../../../media/%s' style='height:90px;'>" % obj.image
    show_image.allow_tags = True #permet de sortir du html#
    show_image.short_description = 'Image'
        
    list_display = ('status','show_image',  'titre', 'lien')
    list_display_links = ('status', 'titre')
    search_fields = ['titre']
    
    def queryset(self, request):
        
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        return qs


admin.site.register(Slider, SliderAdmin)