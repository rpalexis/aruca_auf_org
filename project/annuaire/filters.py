# -*- encoding: utf-8 -*-
from django.conf import settings
from annuaire.models import *
import django_filters


class MembreFilter(django_filters.FilterSet): 
    nom = django_filters.CharFilter(lookup_type='icontains', name='nom')
    etablissement = django_filters.CharFilter(lookup_type='icontains', name='etablissement')
    mots_cles = django_filters.CharFilter(lookup_type='icontains', name='mots_cles')
    axe = django_filters.ChoiceFilter(label="Axe de recherche", required=False, help_text="", choices=(('', 'Sélectionnez un axe de recherche...'), ('1', 'Ressources vivantes naturelles'), ('2', 'Santé humaine et épidémiologie'), ('3', 'Territoires, sciences humaines, cultures et société'), ('4', 'Economie et développement'), ('5', 'Connaissance,exploitation et gestion du milieu physique')))

    class Meta:
        model = Chercheur
        fields = ['nom', 'etablissement', 'axe', 'mots_cles']
        
class EquipeFilter(django_filters.FilterSet): 
    nom = django_filters.CharFilter(lookup_type='icontains', name='nom')
    etablissement = django_filters.CharFilter(lookup_type='icontains', name='etablissement')
    mots_cles = django_filters.CharFilter(lookup_type='icontains', name='mots_cles')
    axe = django_filters.ChoiceFilter(label="Axe de recherche", required=False, help_text="", choices=(('', 'Sélectionnez un axe de recherche...'), ('1', 'Ressources vivantes naturelles'), ('2', 'Santé humaine et épidémiologie'), ('3', 'Territoires, sciences humaines, cultures et société'), ('4', 'Economie et développement'), ('5', 'Connaissance,exploitation et gestion du milieu physique')))

    class Meta:
        model = Equipe
        fields = ['nom', 'etablissement', 'axe', 'mots_cles']