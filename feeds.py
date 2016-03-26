# -*- encoding: utf-8 -*
from django.contrib.syndication.views import Feed
from annuaire.models import *
from itertools import chain

class DerniersAjouts(Feed):
    title = "Derniers ajouts"
    description = "Derniers chercheurs et équipes de recherches ajoutés sur le site"
    link = "/flux-rss/"

    def items(self):
    	chercheur = Chercheur.objects.all().order_by('-date_pub')[:10]
    	equipe = Equipe.objects.all().order_by('-date_pub')[:10]
    	return chain(chercheur, equipe)
        


    def item_title(self, item):
        return "%s %s" % (item.prenom, item.nom)


    def item_description(self, item):
        return item.etablissement
