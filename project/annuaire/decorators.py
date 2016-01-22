# coding: utf-8

from annuaire.models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def chercheur_required(func):
    """Décorateur qui vérifie si un chercheur est connecté."""

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_URL)
        chercheur = request.chercheur
        if chercheur: 
            return func(request, *args, **kwargs)
        else:
            print "PAS COOL"
            return HttpResponseRedirect('/')

    return wrapper