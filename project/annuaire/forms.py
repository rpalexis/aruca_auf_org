# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm, SetPasswordForm as DjangoSetPasswordForm
from django.forms.models import inlineformset_factory
from models import *

class SendPasswordForm(forms.Form):
    email = forms.EmailField(required=True, label="Adresse électronique")
    def clean_email(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        if email:
            try:
                Chercheur.objects.get(courriel=email)
            except:
                raise forms.ValidationError("Cette adresse n'existe pas dans notre base de données.")       
        return email

class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Mot de passe") 
    password_repeat = forms.CharField(widget=forms.PasswordInput(), required=True, label="Confirmez votre mot de passe")

    def clean_password_repeat(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password and password_repeat:
            if password != password_repeat:
                raise forms.ValidationError("Les mots de passe ne concordent pas")
        return password_repeat

class AuthenticationForm(DjangoAuthenticationForm):
    username = forms.CharField(label='Courriel')

class InscriptionCForm(forms.ModelForm):
    class Meta:
        model = Chercheur
        
    def clean_courriel(self):
        """On veut s'assurer qu'il n'y ait pas d'autre utilisateur actif
           avec le même courriel."""
        courriel = self.cleaned_data['courriel']
        print courriel
        existing = Chercheur.objects.filter(courriel=courriel, actif=True)
        if self.instance and self.instance.id:
            existing = existing.exclude(id=self.instance.id)

        else:
            # Nouveau chercheur
            user = User.objects.filter(is_active=True, email=courriel)
            if user.count():
                raise forms.ValidationError('Il existe déjà une fiche pour cette adresse électronique')

        if existing.count():
            raise forms.ValidationError('Il existe déjà une fiche pour cette adresse électronique')
        return courriel
        
class TheseForm(forms.ModelForm):
    class Meta:
        model = These
        fields = ('titre', 'annee', 'directeur', 'etablissement', 'nb_pages')
        
class PublicationForm(forms.ModelForm):
    class Meta:
        model = PublicationsMajeur
        fields = ('auteurs', 'titre', 'revue', 'annee', 'nb_pages')
        
PublicationFormSet = inlineformset_factory(Chercheur, PublicationsMajeur, form=PublicationForm, extra=1)

class attestationForm(forms.Form):
    attestation = forms.BooleanField(required=True,label="J'atteste sur l'honneur l'exactitude des renseignements fournis sur le formulaire d'inscription et j'accepte leur publication en ligne.")
    
class ChercheurFormGroup(object):

    def __init__(self, data=None, chercheur=None):
        try:
            these = chercheur and chercheur.these
        except These.DoesNotExist:
            these = These()
        self.chercheur = InscriptionCForm(data=data, prefix='chercheur', instance=chercheur)
        self.these = TheseForm(data=data, prefix='these', instance=these)
        self.attestation = attestationForm(data=data, prefix='attestation')
        self.publications = PublicationFormSet(data=data, prefix='publication', instance=chercheur)

    @property
    def has_errors(self):
        return bool(self.chercheur.errors or self.these.errors or self.publications.errors or self.attestation.errors)

    def is_valid(self):
        return self.chercheur.is_valid() and self.these.is_valid() and self.publications.is_valid() and self.attestation.is_valid()

    def save(self):
        if self.is_valid():

            # Enregistrer d'abord le chercheur lui-même.
            self.chercheur.save()

            # Puis les objets qui ont des clés étrangères vers nous
            # puisqu'on a besoin d'un id.
            chercheur = self.chercheur.instance
            self.these.instance.chercheur = chercheur
            self.these.save()
            self.publications.instance = chercheur
            self.publications.save()
            return self.chercheur.instance
            
            
class InscriptionEForm(forms.ModelForm):
    class Meta:
        model = Equipe
        
class PublicationFormEquipe(forms.ModelForm):
    class Meta:
        model = PublicationsMajeurEquipe
        fields = ('auteurs', 'titre', 'revue', 'annee', 'nb_pages')
        
PublicationFormSetEquipe = inlineformset_factory(Equipe, PublicationsMajeurEquipe, form=PublicationFormEquipe, extra=1)
            
class EquipeFormGroup(object):

    def __init__(self, data=None, equipe=None):
        self.equipe = InscriptionEForm(data=data, prefix='chercheur', instance=equipe)
        self.attestation = attestationForm(data=data, prefix='attestation')
        self.publications = PublicationFormSetEquipe(data=data, prefix='publication', instance=equipe)

    @property
    def has_errors(self):
        return bool(self.equipe.errors or self.publications.errors or self.attestation.errors)

    def is_valid(self):
        return self.equipe.is_valid() and self.publications.is_valid() and self.attestation.is_valid()

    def save(self):
        if self.is_valid():

            # Enregistrer equipe.
            self.equipe.save()

            # Puis les objets qui ont des clés étrangères vers nous
            # puisqu'on a besoin d'un id.
            equipe = self.equipe.instance
            self.publications.instance = equipe
            self.publications.save()
            return self.equipe.instance
            