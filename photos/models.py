# -*- coding: Utf-8 -*-
from django.db import models

class Album(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nom de l\'album')
    slug = models.SlugField(unique=True)
    texte = models.TextField()
    date_album = models.DateField(null=True, blank=True)
    date_mod = models.DateTimeField('date de modification', auto_now=True)
    actif = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.nom
    
    def get_absolute_url(self):
        return "/album/%s/" %self.id
    
class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos')
    legende = models.CharField(max_length=255, null=True, blank=True, verbose_name='légende')
    image = models.ImageField(null=True, blank=True, upload_to='Album')

    def __unicode__(self):
        return self.legende