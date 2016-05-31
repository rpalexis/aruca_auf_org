# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from auf.django.references.models import Pays
# from django.utils.hashcompat import sha_constructor
from hashlib import sha1 as sha_constructor
#Getting the list of global country
All_Pays = Pays.objects.all()
the_pa = []
for pay in All_Pays:
    a = (str(pay),str(pay))
    the_pa.append(a)

pays_tuple = tuple(the_pa)
#Getting the list of global country

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

langue_choices = (
    ('FR','Francais'),
    ('EN','Anglais'),
    ('ES','Espagnol'),
    ('CR','Creole'),
    ('NOP','Pas d\'autres'),
)

class LaboEquip(models.Model):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'images_pic/photo_labo/{0}'.format(filename)
    def user_directory_path2(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'images_pic/logo_labo/{0}'.format(filename)
    def user_directory_path3(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'images_pic/CV_Resp_Labo/{0}'.format(filename)
    nom = models.CharField("Nom du laboratoire *",max_length=100,help_text="Nom du laboratoire *")
    sigle = models.CharField("Sigle du laboratoire",max_length=50,help_text="Sigle du laboratoire")
    universite = models.CharField("Nom de l'universite d'appartenance *",max_length=100,help_text="Nom de l'universite d'appartenance *")
    faculte = models.CharField("Faculte/Institut/Ecole",max_length=100,help_text="Faculte/Institut/Ecole *")
    disciplinePrinci = models.CharField("Discipline Principle *",max_length=100,help_text="Discipline Principle *")
    disciplineSecond = models.CharField("Discipline Secondaire",max_length=100,help_text="Discipline Secondaire")
    languePrincip = models.CharField("Langue principale de travail *",max_length=5,help_text="Langue principale de travail *",choices=langue_choices)
    autrelangue = models.CharField("Autres langues (de facon significative > 25%) *",max_length=5,help_text="Autres langues (de facon significative > 25%) *",choices=langue_choices)
    anneeCreation = models.CharField("Annee de creation(AAAA) *",max_length=5,help_text="Annee de creation(AAAA) *")
    anneeLastEval = models.CharField("Annee de la derniere evaluation (AAAA)* <i>inscrire 0000 si le laboratoire n'a jamais ete evalue</i>",max_length=5,help_text="Annee de la derniere evaluation (AAAA)* <i>inscrire 0000 si le laboratoire n'a jamais ete evalue</i>")
    adresse = models.CharField("Adresse *",max_length=100,help_text="Adresse *")
    ville = models.CharField("Ville *",max_length=100,help_text="Ville *")
    telNum = models.CharField("Numero de telephone *",max_length=20,help_text="Numero de telephone *")
    email = models.EmailField("Adresse mail generale *",max_length=100,help_text="Adresse mail generale *")
    siteInternet = models.URLField("Site internet",max_length=200,help_text="Site internet")
    pays = models.CharField("Pays *",max_length=100,help_text="Pays *",choices=pays_tuple)
    partenariatinter = models.TextField("Principaux partenariats internationaux *",help_text="Principaux partenariats internationaux *")
    equipement =  models.TextField("Principaux equipements, terrains, materiels *",help_text="Principaux equipements, terrains, materiels *")
    photoLabo = models.ImageField("Joindre une photo de votre laboratoire/equipe de recherche *",help_text="Joindre une photo de votre laboratoire/equipe de recherche *",upload_to=user_directory_path)
    logoLabo = models.ImageField("Joindre une photo de votre laboratoire/equipe de recherche *",help_text="Joindre une photo de votre laboratoire/equipe de recherche *",upload_to=user_directory_path2)

    #Informations sur le responsable du laboratoire / equipe de recherche
    nom = models.CharField("Nom *",max_length=100,help_text="Nom *")
    prenom = models.CharField("Prenom *",max_length=100,help_text="Prenom *")
    rangUniv = models.CharField("Rang Universitaire *",max_length=100,help_text="Rang Universitaire *")
    discipline = models.CharField("Discipline *",max_length=100,help_text="Discipline *")
    autreFct = models.CharField("Autre Fonction ",max_length=200,help_text="Autre Fonction *")
    phoneNumb = models.CharField("Numero de telephone direct *",max_length=200,help_text="Numero de telephone direct *")
    afficheNumPub = models.BooleanField("Cocher pour afficher le numero publiquement",help_text="Cocher pour afficher le numero publiquement")
    emailRsp = models.EmailField("Email direct *",max_length=100,help_text="Email direct *")
    afficheMailPub = models.BooleanField("Cocher pour l'email publiquement",help_text="Cocher pour l'email publiquement")
    cvResp = models.FileField("Joindre CV",help_text="Joindre CV",upload_to=user_directory_path3)
    effectifs = models.FloatField("Effectifs <i>(Ne sont comptabilises que les chercheurs permanents.Ne pas comptabiliser les chercheurs visiteurs ou collaborations occasionnelles. Ecrire 0 si la categorie n'est pas concernee)</i>",help_text="Effectifs <i>(Ne sont comptabilises que les chercheurs permanents.Ne pas comptabiliser les chercheurs visiteurs ou collaborations occasionnelles. Ecrire 0 si la categorie n'est pas concernee)</i>")
    profUniv = models.FloatField("Professeurs des universites (ou equivalent) *",help_text="Professeurs des universites (ou equivalent) *")
    metConf = models.FloatField("Maitres de conference (ou equivalent) *",help_text="Maitres de conference (ou equivalent) *")
    assistants = models.FloatField("Assistants (ou equivalents) *",help_text="Assistants (ou equivalents) *")
    doctorants = models.FloatField("Doctorants *",help_text="Doctorants *")
    autresComp = models.FloatField("Autres *",help_text="Autres *")
    listeChercheurs = models.TextField("Liste des chercheurs de l'unite *",help_text="Liste des chercheurs de l'unite *")

    #Informations sur le responsable du laboratoire / equipe de recherche

    #recherche
    probAxeRech = models.CharField("Problematiques et axes de recherches *",max_length=200,help_text="Problematiques et axes de recherches *")
    mots_cles = models.CharField("Mots cles *",max_length=200,help_text="Mots cles *")
    nombrePub = models.FloatField("Nombre de publications de rang international (5 dernires annees)*",help_text="Nombre de publications de rang international (5 dernires annees)*")
    autrePub = models.FloatField("Autres publications dont actes de colloque (5 dernieres annees) *",help_text="Autres publications dont actes de colloque (5 dernieres annees) *")
    theseSout = models.FloatField("Nombre de theses soutenues (5 dernieres annees) *",help_text="Nombre de theses soutenues (5 dernieres annees) *")

    infoComple = models.TextField("Informations Complementaires",help_text="Informations Complementaires")

    #recherche

    show = models.CharField("A afficher publiquement",max_length=3,choices=(
        ('1','Visible sur le Site'),
        ('0','Invisible sur le Site'),
    ),default=0)



#Added deuxieme lot
