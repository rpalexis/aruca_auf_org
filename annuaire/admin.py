# -*- coding: Utf-8 -*-
from annuaire.models import *
from django.contrib import admin

class TheseInline(admin.TabularInline):
    model = These
    
class PublicationsInline(admin.TabularInline):
    model = PublicationsMajeur
    
class PublicationsEquipeInline(admin.TabularInline):
    model = PublicationsMajeurEquipe

class ChercheurAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'prenom', 'axe', 'etablissement', 'langue', 'actif')
    
    fieldsets = [
        ('Propriété de la Fiche', {'fields': ['langue', 'actif'], 'classes': ['wide']}),
        ('Etablissement', {'fields': ['etablissement', 'etablissement_autre_nom', 'etablissement_autre_pays'], 'classes': ['wide']}),
        ('Informations personnelles', {'fields': ['genre', 'nom', 'prenom', 'courriel', 'afficher_courriel', 'site', 'telephone', 'telecopie', 'diplome'], 'classes': ['wide']}),
        ('Enseignements', {'fields': ['axe', 'discipline', 'theme_recherche', 'mots_cles'], 'classes': ['wide']}),
        ('Equipement', {'fields': ['equipement', 'laboratoire', 'terrain'], 'classes': ['collapse']}),
        ('Valorisation et autres', {'fields': ['valorisation', 'partenaires', 'doctorants', 'stagiaire'], 'classes': ['wide']}),
        ('Publications', {'fields': ['publicationsInternational', 'publicationsAutre', 'publicationsColloc', 'communication'], 'classes': ['wide']}),
        ('Equipe de recherche', {'fields': ['equipe', 'domaine'], 'classes': ['wide']}),
    ]
    
    inlines = [PublicationsInline, TheseInline,]
    
class EquipeAdmin(admin.ModelAdmin):
    
    list_display = ('intitule', 'prenom', 'axe', 'etablissement', 'langue', 'actif')
    
    fieldsets = [
        ('Propriété de la Fiche', {'fields': ['langue', 'actif'], 'classes': ['wide']}),
        ('Présentation équipe', {'fields': ['intitule', 'etablissement', 'etablissement_autre_nom', 'etablissement_autre_pays', 'date_creation', 'date_evaluation', 'presentation'], 'classes': ['wide']}),
        ('Information responsable', {'fields': ['genre', 'nom', 'prenom', 'courriel', 'afficher_courriel', 'site', 'telephone', 'telecopie'], 'classes': ['wide']}),
        ('Effectifs', {'fields': ['prof', 'maitre', 'assistant', 'chercheur', 'autres'], 'classes': ['wide']}),
        ('Enseignements', {'fields': ['axe', 'problematique', 'mots_cles'], 'classes': ['wide']}),
        ('Equipement', {'fields': ['equipement', 'laboratoire', 'terrain'], 'classes': ['collapse']}),
        ('Partenariats et réseaux', {'fields': ['valorisation', 'partenaires', 'enseignant', 'doctorants', 'stagiaire'], 'classes': ['wide']}),
        ('Publications', {'fields': ['publicationsInternational', 'publicationsAutre', 'publicationsColloc', 'communication'], 'classes': ['wide']}),
        ('Informations complémentaires éventuelles', {'fields': ['complement'], 'classes': ['collapse']}),
    ]
    
    inlines = [PublicationsEquipeInline]

admin.site.register(Chercheur, ChercheurAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(These)
admin.site.register(PublicationsMajeur)
admin.site.register(PublicationsMajeurEquipe)
