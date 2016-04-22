# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
#python2 code handling

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.models import RequestSite, Site
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse as url
from django.utils.http import int_to_base36, base36_to_int
from django.conf import settings
from django.shortcuts import render_to_response, render, redirect, get_object_or_404, get_list_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.template.loader import get_template #, loader
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from annuaire.utils import get_django_user_for_email, get_username_from_email, create_ldap_hash, check_ldap_hash

from annuaire.decorators import chercheur_required
from annuaire.models import *
from annuaire.forms import *
from annuaire.filters import *



def contact(request):
    contact_form = ContactForm()
    return render_to_response('contact.html', {'contact_form' : contact_form})

def accueil(request):
    return render_to_response('accueil.html', context_instance=RequestContext(request))


def InscriptionChercheur(request):
    # forms = {}
    if request.method == 'POST':
        print("I'm in the post in the view")
        forms = ChercheurFormGroup(request.POST)
        if forms.is_valid():
            print("I'm in the validation of form")
            chercheur = forms.save()
            id_base36 = chercheur.id #int_to_base36
            token = chercheur.activation_token()
            template = get_template('activation_email.txt')
            domain = RequestSite(request).domain
            print(domain)
            message = template.render(Context({
                'chercheur': chercheur,
                'id_base36': id_base36,
                'token': token,
                'domain': domain
            }))
            print(message)
            #The url for the user's connection
            #   http://{{ domain }}{% url chercheur_activation id_base36=id_base36, token=token %}
            send_mail(
                'Votre inscription au site ARUCA',
                message, 'rulxphilome.alexis@gmail.com', [chercheur.courriel]
            )
            return HttpResponseRedirect('/annuaire/validation/')
    else:
        forms = ChercheurFormGroup()
        print("I'm in the GET part")

    # return render_to_response('inscriptionC.html', {'forms' : forms}, context_instance=RequestContext(request))
    return render(request,'inscriptionC.html',{'forms':forms})

@chercheur_required
def perso(request):
    """Espace chercheur (espace personnel du chercheur)"""
    chercheur = Chercheur.objects.filter(courriel = request.user.email)[0]  #request.chercheur
    modification = request.GET.get('modification')
    list_publi = PublicationsMajeur.objects.filter(chercheur=chercheur)
    list_these = These.objects.filter(chercheur=chercheur)
    return render(request, "perso.html", {
        'chercheur': chercheur,
        'modification': modification, 'list_publi': list_publi, 'list_these': list_these
    })

@csrf_protect
@login_required
def password_change(request,
                    template_name='registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm):
    if post_change_redirect is None:
        post_change_redirect = url(
            'django.contrib.auth.views.password_change_done'
        )
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()

            # Mot de passe pour LDAP
            username = request.user.email
            authldap, created = \
                    AuthLDAP.objects.get_or_create(username=username)
            password = form.cleaned_data.get('new_password1')
            authldap.ldap_hash = create_ldap_hash(password)
            authldap.save()

            return redirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    return render(request, template_name, {'form': form})


@chercheur_required
def desinscription(request):
    """Désinscription du chercheur"""
    chercheur = request.chercheur
    if request.method == 'POST':
        if request.POST.get('confirmer'):
            chercheur.actif = False
            chercheur.save()
            request.flash['message'] = \
                    "Vous avez été désinscrit du répertoire des chercheurs."
            return redirect('django.contrib.auth.views.logout')
        else:
            request.flash['message'] = "Opération annulée."
            return redirect('annuaire.views.perso')
    return render(request, "desinscription.html")

@chercheur_required
@never_cache
def edit(request):
    """Edition d'un chercheur"""
    chercheur = Chercheur.objects.filter(courriel = request.user.email)[0] #request.chercheur
    if request.method == 'POST':
        forms = ChercheurFormGroup(request.POST, chercheur=chercheur)
        if forms.is_valid():
            chercheur.actif = True
            forms.save()
            print("BIEN MODIFIE on retourne a la page perso")
            #request.flash['message'] = "Votre fiche a bien été enregistrée."
            return redirect('annuaire.views.perso')
    else:
        forms = ChercheurFormGroup(chercheur=chercheur)

    return render(request, "edit.html", {
        'forms': forms,
        'chercheur': chercheur
    })


def activation(request, id_base36, token):
    """Activation d'un chercheur"""
    id = id_base36 #base36_to_int
    chercheur = get_object_or_404(Chercheur.objects.all(), id=id)
    if token == chercheur.activation_token():
        validlink = True
        if request.method == 'POST':
            form = SetPasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                email = chercheur.courriel
                chercheur.actif = True
                user = get_django_user_for_email(email)
                user.set_password(password)
                user.save()
                # chercheur.user = user
                chercheur.save()
                # Auto-login
                auth_login(
                    request, authenticate(username= get_username_from_email(email), password=password)
                )
                return redirect('annuaire.views.perso')
        else:
            form = SetPasswordForm()
    else:
        form = None
        validlink = False
    return render(request, 'activation.html', {
        'form': form,
        'validlink': validlink
    })


def chercheur_detail(request, id):
    chercheur_detail = Chercheur.objects.get(id=id)
    list_publi = PublicationsMajeur.objects.filter(chercheur=id)
    list_these = These.objects.filter(chercheur=id)
    return render_to_response('chercheur.html', {'chercheur_detail': chercheur_detail, 'list_publi': list_publi, 'list_these': list_these}, context_instance = RequestContext(request))


def list_chercheur(request):
    dictFilter = {}
    langue = request.LANGUAGE_CODE
    print(langue)
    if langue == 'fr':
        langue = 'f'
    else:
        langue = 'e'
    chercheurs_list = MembreFilter(request.GET or None, queryset = Chercheur.objects.filter(**dictFilter).filter(langue=langue))

    return render_to_response('chercheurs.html', {'chercheurs_list': chercheurs_list, 'ChercherCForm': chercheurs_list.form}, context_instance = RequestContext(request))

def InscriptionEquipe(request):

    if request.method == 'POST':
        forms = EquipeFormGroup(request.POST)
        if forms.is_valid():
            equip = forms.save()
            #send_mail('Inscription au site ARUCA', 'Votre équipe de chercheurs est inscrit sur le site ARUCA. merci','webmestre@auf.org',[equip.courriel])
            return HttpResponseRedirect('/validation_equipe/')
    else:
        forms = EquipeFormGroup()

    return render_to_response('inscriptionE.html', {'forms' : forms}, context_instance=RequestContext(request))

def equipe(request, id):
    equipe_detail = Equipe.objects.get(id=id)
    list_publi = PublicationsMajeurEquipe.objects.filter(chercheur=id)
    return render_to_response('equipe.html', {'equipe_detail': equipe_detail, 'list_publi': list_publi}, context_instance = RequestContext(request))

def list_equipe(request):
    dictFilter = {}
    langue = request.LANGUAGE_CODE
    if langue == 'fr':
        langue = 'f'
    else:
        langue = 'e'
    equipe_list = EquipeFilter(request.GET or None, queryset = Equipe.objects.filter(**dictFilter).filter(langue=langue))

    return render_to_response('equipes.html', {'equipe_list': equipe_list, 'EquipeCForm': equipe_list.form}, context_instance = RequestContext(request))

def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME):
    "The Django login view, but using a custom form."
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        print(request.POST.get('username'))
        posted_data = {'username':get_username_from_email(request.POST.get('username')),
        'password':request.POST.get('password'),
        'csrfmiddlewaretoken':request.POST.get('csrfmiddlewaretoken')}
        form = AuthenticationForm(data=posted_data)

        print(posted_data)
        # print(form.get_user())
        if form.is_valid():
            # Light security check -- make sure redirect_to isn't garbage.
            if not redirect_to or ' ' in redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Mot de passe pour LDAP
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            authldap, created = \
                    AuthLDAP.objects.get_or_create(username=username)
            if created or not check_ldap_hash(authldap.ldap_hash, password):
                authldap.ldap_hash = create_ldap_hash(password)
                authldap.save()

            # Okay, security checks complete. Log the user in.
            print(form.get_user())
            auth_login(request, form.get_user())


            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return redirect(redirect_to)

    else:
        form = AuthenticationForm(request)
    request.session.set_test_cookie()

    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)

    return render(request, template_name, {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    })
login = never_cache(login)

@csrf_protect
@login_required
def password_change(request,
                    template_name='password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm):
    if post_change_redirect is None:
        post_change_redirect = url(
            'django.contrib.auth.views.password_change_done'
        )
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()

            # Mot de passe pour LDAP
            username = request.user.email
            authldap, created = \
                    AuthLDAP.objects.get_or_create(username=username)
            password = form.cleaned_data.get('new_password1')
            authldap.ldap_hash = create_ldap_hash(password)
            authldap.save()

            return redirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    return render(request, template_name, {'form': form})
