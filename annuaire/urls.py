# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('annuaire.views',
    url(r'^$', 'accueil',name="aruca_home"),
    url(r'^chercheurs/$', 'list_chercheur',name="list_chercheur"),
    url(r'^chercheurs/(?P<id>[-\w]+)/$', 'chercheur_detail',name="chercheur_detail"),
    # url(r'^inscription-chercheur/$', 'InscriptionChercheur', name='chercheur_inscription'),
    url(r'^chercheur/activation/(?P<id_base36>.*)/(?P<token>.*)/$','activation', name='chercheur_activation'),
    url(r'^espace_utilisateur/$', 'perso'),
    url(r'^chercheur/edit/$', 'edit'),
    url(r'^chercheur/desinscription/$', 'desinscription'),
    url(r'^validation/$', TemplateView.as_view(template_name='validation.html'), name='Validation_chercheur'),
    url(r'^equipes/$', 'list_equipe'),
    url(r'^equipes/(?P<id>[-\w]+)/$', 'equipe',name="team"),
    url(r'^inscription-equipe/$', 'InscriptionEquipe',name="insc_Equipe"),
    url(r'^validation_equipe/$', TemplateView.as_view(template_name='validation_equipe.html'), name='Validation_equipe'),
    url(r'^connexion/$', 'login', kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^actualites/$', 'actual',name='actualites'),
    url(r'^appels_offres/$', 'aos',name='appelO'),
    url(r'^liens_utiles/$', 'usefull_link',name='usefull_link'),
    url(r'presentation/$', 'presentation',name='presentation'),
    url(r'equipe_laboratoire/$', 'equipe_laboratoire',name='equipe_laboratoire'),

    # Espace utilisateurs
    url(r'^creation_compte/$', 'creation_compte',name='creation_compte'),
    # Espace utilisateurs
)

urlpatterns += patterns ('',
    url(r'^deconnexion/$', 'django.contrib.auth.views.logout', kwargs={'template_name': 'accueil.html'}, name='chercheurs_logout'),
    url(r'^chercheur/changement-mdp/$', 'annuaire.views.password_change',
        kwargs={
            'template_name': 'password_change_form.html',
            'post_change_redirect': '/chercheur/changement-mdp-fini/'
        },
        name='chercheurs-password-change'),
    url(r'^chercheur/changement-mdp-fini/$',
        'django.contrib.auth.views.password_change_done',
        kwargs={'template_name': 'password_change_done.html'},
        name='chercheurs-password-change-done'),
    # Oublié mot de passe
    url(r'^chercheur/oubli-mdp/$', 'django.contrib.auth.views.password_reset', kwargs={
            'template_name': 'password_reset_form.html',
            'email_template_name': 'password_reset_email.txt',
            'post_reset_redirect': '/chercheur/oubli-mdp-envoye/'
        },
        name='chercheurs-password-reset'),
    url(r'^chercheur/oubli-mdp-envoye/$', 'django.contrib.auth.views.password_reset_done', kwargs={'template_name': 'password_reset_done.html'},
        name='chercheurs-password-reset-done'),
    url(r'^chercheur/oubli-mdp-retour/(?P<uidb36>.*)/(?P<token>.*)/$', 'django.contrib.auth.views.password_reset_confirm', kwargs={'template_name': 'password_reset_confirm.html'},
        name='chercheurs_password_reset_confirm'),
    url(r'^chercheur/oubli-mdp-fini/$', 'django.contrib.auth.views.password_reset_complete', kwargs={'template_name': 'password_reset_complete.html'}),
)
