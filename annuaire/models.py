# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from auf.django.references.models import Pays
# from django.utils.hashcompat import sha_constructor
from hashlib import sha1 as sha_constructor


GENRE_CHOICES = (('m', 'Homme'), ('f', 'Femme'))
LANGUE_CHOICES = (('f', 'Francais'), ('e', 'Espagnol'))
AXE_CHOICES = (('1', 'Ressources vivantes naturelles'), ('2', 'Santé humaine et épidémiologie'), ('3', 'Territoires, sciences humaines, cultures et société'), ('4', 'Economie et développement'), ('5', 'Connaissance,exploitation et gestion du milieu physique'))
class Chercheur(models.Model):
    langue = models.CharField(max_length=1, choices=LANGUE_CHOICES)
    etablissement = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'Université')
    etablissement_autre_nom = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'faculté/institut/école')
    etablissement_autre_pays = models.ForeignKey(Pays, null = True, blank=True, db_column='etablissement_autre_pays',
                                                 to_field='code', related_name='etablissement_autre_pays',
                                                 verbose_name = "pays de l'établissement")
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=128, verbose_name='prénom')
    courriel = models.EmailField(max_length=128, null=False, blank=False, verbose_name="courriel")
    afficher_courriel = models.BooleanField(default=True)
    site = models.URLField(max_length=200, null=True, blank=True, verbose_name="Site Internet")
    telephone = models.CharField(max_length=32, null=True, blank=True, verbose_name='numéro de téléphone')
    telecopie = models.CharField(max_length=32, null=True, blank=True, verbose_name='numéro de télécopie')
    axe = models.CharField(max_length=1, choices=AXE_CHOICES, verbose_name='Axe de recherche')
    mots_cles = models.TextField(max_length=255, null=True, blank=True, verbose_name='mots-clés')
    diplome = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'diplôme le plus élevé')
    discipline = models.TextField(blank=True, verbose_name='Enseignements dispensés')
    theme_recherche = models.TextField(blank=True, verbose_name='Problématique et description de la recherche')
    equipement = models.TextField(blank=True, verbose_name='Equipement disponible')
    laboratoire = models.TextField(blank=True, verbose_name='Laboratoire')
    terrain = models.TextField(blank=True, verbose_name='Terrain')
    valorisation = models.TextField(blank=True, verbose_name='Valorisation et domaine de compétence')
    partenaires = models.CharField(max_length=255, blank=True, verbose_name='Partenaires')
    doctorants = models.CharField(max_length=255, blank=True)
    stagiaire = models.CharField(max_length=255, blank=True, verbose_name='Autres stagiaires')
    publicationsInternational = models.IntegerField(default=0, blank=True, verbose_name='Nombre de publication de niveau internationales')
    publicationsAutre = models.IntegerField(default=0, blank=True, verbose_name='Autres publications')
    publicationsColloc = models.IntegerField(default=0, blank=True, verbose_name='Nombre de publication ayant fait l\'objet de publication dans actes de colloque')
    communication = models.IntegerField(default=0, blank=True, verbose_name='Autres communications')
    equipe = models.BooleanField(verbose_name='Etes-vous intéressé à créer ou intégrer une équipe de recherche?')
    domaine = models.CharField(max_length=255,verbose_name='Si oui dans quel domaine?', blank=True)
    date_mod = models.DateTimeField('date de modification', auto_now=True)
    date_pub = models.DateField('date de creation',auto_now_add=True)
    actif = models.BooleanField(default=False)

    def activation_token(self):
        enc = settings.SECRET_KEY + str(self.id)
        return sha_constructor(enc.encode('utf-8')).hexdigest()[::2]

    def get_absolute_url(self):
        return "/annuaire/chercheurs/%s/" %self.id

    class Meta:
        ordering = ["nom", "prenom", "langue"]


class These(models.Model):
    chercheur = models.OneToOneField(Chercheur, primary_key=True)
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Titre')
    annee = models.IntegerField(null=True, blank=True, verbose_name='Année de soutenance (réalisée ou prévue)')
    directeur = models.CharField(max_length=255, null=True, blank=True, verbose_name='Directeur')
    etablissement = models.CharField(max_length=255, null=True, blank=True, verbose_name='Établissement de soutenance')
    nb_pages = models.IntegerField(verbose_name='Nombre de pages', null=True, blank=True)

    def __str__(self):
        return self.titre

class PublicationsMajeur(models.Model):
    chercheur = models.ForeignKey(Chercheur, related_name='publications')
    auteurs = models.CharField(max_length=255, blank=True, verbose_name='auteur(s)')
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name='titre')
    revue = models.CharField(max_length=255, null=True, blank=True, verbose_name='revue')
    annee = models.CharField(max_length=255, null=True, blank=True, verbose_name='Date de publication')
    nb_pages = models.CharField(max_length=255, null=True, blank=True, verbose_name='nombre de pages')

    def __str__(self):
        return self.titre


class Equipe(models.Model):
    langue = models.CharField(max_length=1, choices=LANGUE_CHOICES)
    etablissement = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'Université')
    etablissement_autre_nom = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'Faculté/institut/école')
    etablissement_autre_pays = models.ForeignKey(Pays, null = True, blank=True, db_column='etablissement_autre_pays',
                                                 to_field='code', related_name='etablissement_autre_pays_equipe',
                                                 verbose_name = "Pays de l'établissement")
    intitule = models.CharField(max_length=255, verbose_name='Intitulé de l\'équipe de recherche')
    axe = models.CharField(max_length=1, choices=AXE_CHOICES)
    date_creation = models.DateField('Date de creation', blank=True, null=True)
    date_evaluation = models.DateField('Date de la dernière évaluation', blank=True, null=True)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    nom = models.CharField(max_length=255, verbose_name='Nom du responsable')
    prenom = models.CharField(max_length=128, verbose_name='Prénom du responsable')
    courriel = models.EmailField(max_length=128, null=False, blank=False, verbose_name="courriel")
    afficher_courriel = models.BooleanField(default=True, verbose_name='Afficher le courriel')
    site = models.URLField(max_length=200, null=True, blank=True, verbose_name="Site Internet")
    telephone = models.CharField(max_length=32, null=True, blank=True, verbose_name='Numéro de téléphone')
    telecopie = models.CharField(max_length=32, null=True, blank=True, verbose_name='Numéro de télécopie')
    prof = models.IntegerField(default=0, blank=True, verbose_name='Nombre de professeurs')
    maitre = models.IntegerField(default=0, blank=True, verbose_name='Nombre de maîtres de conférence')
    assistant = models.IntegerField(default=0, blank=True, verbose_name='Nombre d\'assistants')
    chercheur = models.IntegerField(default=0, blank=True, verbose_name='Nombre de chercheurs')
    autres = models.IntegerField(default=0, blank=True, verbose_name='Autres')
    presentation = models.TextField(blank=True, verbose_name='Présentation')
    problematique = models.TextField(blank=True, verbose_name='Problématique et description succinte de la recherche')
    mots_cles = models.TextField(null=True, blank=True, verbose_name='mots-clés')
    equipement = models.TextField(blank=True, verbose_name='Equipement disponible')
    laboratoire = models.TextField(blank=True, verbose_name='Laboratoire')
    terrain = models.TextField(blank=True, verbose_name='Terrain')
    valorisation = models.TextField(blank=True, verbose_name='Valorisation et domaine de compétence')
    partenaires = models.TextField(blank=True, verbose_name='Partenaires')
    enseignant = models.TextField(blank=True, verbose_name='Liste des enseignants-chercheurs de l\'unité')
    doctorants = models.IntegerField(default=0, blank=True)
    stagiaire = models.IntegerField(default=0, blank=True, verbose_name='Autres stagiaires')
    publicationsInternational = models.IntegerField(default=0, blank=True, verbose_name='Nombre de publication de niveau internationales')
    publicationsAutre = models.IntegerField(default=0, blank=True, verbose_name='Autres publications')
    publicationsColloc = models.IntegerField(default=0, blank=True, verbose_name='Nombre de publication ayant fait l\'objet de publication dans actes de colloque')
    communication = models.IntegerField(default=0, blank=True, verbose_name='Autres communications')
    complement = models.TextField(blank=True, verbose_name='Informations complémentaires')
    date_mod = models.DateTimeField('date de modification', auto_now=True)
    date_pub = models.DateField('date de publication',auto_now_add=True)
    actif = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/annuaire/equipes/%s/" %self.id

    class Meta:
        ordering = ["nom", "prenom", "langue"]

class PublicationsMajeurEquipe(models.Model):
    chercheur = models.ForeignKey(Equipe, related_name='publications')
    auteurs = models.CharField(max_length=255, blank=True, verbose_name='auteur(s)')
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name='titre')
    revue = models.CharField(max_length=255, null=True, blank=True, verbose_name='revue')
    annee = models.CharField(max_length=255, null=True, blank=True, verbose_name='Date de publication')
    nb_pages = models.CharField(max_length=255, null=True, blank=True, verbose_name='nombre de pages')

    def __str__(self):
        return self.titre

class AuthLDAP(models.Model):
    username = models.CharField('utilisateur', max_length=255, unique=True)
    ldap_hash = models.CharField('hash LDAP', max_length=255)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

#Added deuxieme lot
chx_type = (
    ("1","Actualites"),
    ("2","Appels d'Offres"),
)
class ActualitesAO(models.Model):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        if(instance.type_artl == "1"):
            return 'images_pic/Actualites_imgs/{0}'.format(filename)
        else:
            return 'images_pic/AO_imgs/{0}'.format(filename)

    type_artl = models.CharField("Types de la publication *",max_length=2,help_text="Types de la publication *",choices=chx_type)
    titre_artl = models.CharField("Titre de la publication *",max_length=100,help_text="Titre de la publication *")
    description_artl = models.TextField("Description de la publication *",max_length=500,help_text="Description de la publication *")
    image_artl = models.ImageField(upload_to=user_directory_path,help_text="Image de la publication")
    lien_artl = models.URLField("Lien pour la publication *",help_text="Lien pour la publication *")
#Added deuxieme lot
