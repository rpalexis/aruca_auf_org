# -*- encoding: utf-8 -*-
from django.db import models

class Appel_Offre(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='appel_offre')
    date_fin = models.DateField(null=True, blank=True)
    date_fin2 = models.CharField(max_length=1, null=True, blank=True, choices=(('1', '1 Moi avant le début des manifestations'), ('2', '2 Mois avant le début des manifestations'), ('3', '3 Mois avant le début des manifestations'), ('4', '4 Mois avant le début des manifestations'), ('5', '5 Mois avant le début des manifestations'), ('6', 'Permanent')))
    date_pub = models.DateTimeField('date de creation', auto_now=True)
    date_mod = models.DateTimeField('date de derniere modification', auto_now_add=True)
    status = models.CharField(max_length=1, default='3', null=False, blank=False, choices=(('1', 'En cours de redaction'), ('2', 'Propose a la publication'), ('3', 'Publie en Ligne'), ('4', 'A supprimer')))
    
    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre 

    def get_absolute_url(self):
        return "/appels-offre/%s/" %self.slug