from django.db import models
from auf.django.references.models import Pays
# Create your models here.

#Getting the list of global country
All_Pays = Pays.objects.all()
the_pa = []
for pay in All_Pays:
    a = (str(pay),str(pay))
    the_pa.append(a)

pays_tuple = tuple(the_pa)
#Getting the list of global country

statut_choices = (
    ('MCA','Membre du Conseil d\'Administration'),
    ('MCAD','Membre du Conseil Academique'),
    ('CG','Coordonateur General'),
)
sexe_choices = (
    ('h','Homme'),
    ('f','Femme'),
)
discipline_choices = (
    ('SCI','Sciences Informatiques'),
    ('MD','Medecine'),
    ('OD','Odontologie'),
)
diplome_obt_choices = (
    ('LC','Licence ou equivalent'),
    ('MS','Master'),
    ('DT','Doctorat'),
)
langue_choices = (
    ('FR','Francais'),
    ('EN','Anglais'),
    ('ES','Espagnol'),
    ('CR','Creole'),
)
langue_choices_autres = (
    ('NOP','Pas d\'autres'),
    ('FR','Francais'),
    ('EN','Anglais'),
    ('ES','Espagnol'),
    ('CR','Creole'),
)
class InstanceCandidature(models.Model):
    """
        Model pour gestions formulaire de participation aux instances de la chaire
    """
    # IMP Methode
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'pdf_files/candidat_inst/user_{0}/{1}'.format(instance.mail_direct, filename)

    sexe = models.CharField("Genre du Candidat",max_length=10,help_text="Genre du Candidat",choices = sexe_choices)
    nom = models.CharField("Nom du Candidat",max_length=50,help_text="Nom du Candidat")
    prenom = models.CharField("Prenom du Candidat",max_length=50,help_text="Prenom du Candidat")
    date_naissance = models.DateField("Date de Naissance",help_text="Date de Naissance")
    pays_nationalite = models.CharField(
        "Pays de Nationnalite",
        max_length=100,
        help_text = "Pays de Nationnalite",
        choices = pays_tuple
    )
    adresse_residence = models.CharField("Adresse de residence du Candidat",max_length=100,help_text="Adresse de residence du Candidat")
    ville_residence = models.CharField("Ville de residence du Candidat",max_length=100,help_text="Ville de residence du Candidat")
    pays_residence = models.CharField(
        "Pays de Residence",
        max_length=100,
        help_text = "Pays de Residence",
        choices = pays_tuple
    )
    numero_telephone_direct = models.CharField("Numéro de téléphone direct*",max_length=15,help_text="Numéro de téléphone direct*")
    mail_direct = models.EmailField("Adresse email direct",max_length=254,help_text="Adresse email direct",unique=True)
    etablissement_universitaire_1 = models.CharField("Etablissement Universitaire de Rattachement",max_length=100,help_text="Etablissement Universitaire de Rattachement")
    etabliseement_universitaire_autres = models.CharField("Autres universites que l'etablissement de rattachement dans lesquelles vous intervenez regulierement",max_length=254,help_text="Autres universites que l'etablissement de rattachement dans lesquelles vous intervenez regulierement")
    discipline_scient_gnrl = models.CharField("Discipline Scientifiques Principales",max_length=10,help_text="Discipline Scientifiques Principales")
    fonction_academique_now = models.CharField("Fonctions academiques actuellement exercees",max_length=100,help_text="Fonctions academiques actuellement exercees")
    fonction_academique_autre = models.CharField("Autres fonctions academiques actuellement exercees",max_length=100,help_text="Autres fonctions academiques actuellement exercees")
    pls_haut_diplome = models.CharField("Plus haut diplome obtenu",max_length=10,choices=diplome_obt_choices,help_text="Plus haut diplome obtenu")
    annee_obt = models.CharField("Annee d'obtention",max_length=5,help_text="Annee d'obtention")
    langue_travail_prin = models.CharField("Langue principale de travail",max_length=5,choices=langue_choices,help_text="Langue principale de travail")
    autre_langue_prin = models.CharField("Autre langue principale",max_length=50,help_text="Autre langue principale")
    langue_maitrise = models.CharField("Autres langues maitrise",max_length=5,choices=langue_choices_autres,help_text="Autres langues maitrise")
    autre_langue_maitrise = models.CharField("Autre autres langues maitrise",max_length=50,help_text="Autre autres langues maitrise")
    implication_academique = models.TextField("Votre implication academique et ou en recherche sur des problematiques caribeennes",help_text="Votre implication academique et ou en recherche sur des problematiques caribeennes")
    synthese_principale = models.TextField("Synthes des principales responsabilites academiques,scientifiques,politiques,publiques,exercees",help_text="Synthes des principales responsabilites academiques,scientifiques,politiques,publiques,exercees")
    ambition_pr_ciec = models.TextField("Vos ambitions pour le CIEC dans les fonctions auxquelles vous postulez",help_text="Vos ambitions pour le CIEC dans les fonctions auxquelles vous postulez")
    avantage_comparatif = models.TextField("Vos avantages comparatifs dans les fonctions auxquelles vous postulez",help_text="Vos avantages comparatifs dans les fonctions auxquelles vous postulez")
    cv_detaille = models.FileField(upload_to=user_directory_path,help_text="Telecharger votre CV detaille")
    lettre_soutien = models.FileField(upload_to=user_directory_path,help_text="Telecharger votre lettre de soutien du plus haut responsable de votre etablissement")

    # Common attribute
    show = models.CharField("A afficher publiquement",max_length=3,choices=(
        ('1','Visible sur le Site'),
        ('0','Invisible sur le Site'),
    ),default=0)
#Fin formulaires InstanceCandidature
statut_candidatures_mbr = (
    ('MT','Membre Titulaire'),
    ('MO','Membre Observateur'),
)
off_status = (
    ('EPu','Etablissement Public'),
    ('EPr','Etablissement Prive'),

)
fct_res_etabl = (
    ('RCT','Recteur'),
    ('DIR','Directeur'),
)

class CandidatMembre(models.Model):
    """
        Model pour gestions formulaire d'adheration a la CIEC
    """
    #Upload function
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'pdf_files/candidat_mbr/user_{0}/{1}'.format(instance.mail_direct, filename)

    #Informations sur l'etablissement
    etabl_nom = models.CharField("Nom de l'etablissement *",max_length=200,help_text="Nom de l'etablissement *")
    etabl_sigle = models.CharField("Sigle de l'etablissement *",max_length=100,help_text="Sigle de l'etablissement *")
    etabl_annee_creation = models.CharField("Annee de creation etablissement *",max_length=5,help_text="Annee de creation etablissement *")
    etabl_statut_officiel = models.CharField("Statut Officiel *",max_length=5,help_text="Statut Officiel *",choices=off_status)
    etabl_adresse = models.CharField("Adresse *",max_length=100,help_text="Adresse *")
    etabl_ville = models.CharField("Ville *",max_length=100,help_text="Ville *")
    etabl_phone_number = models.CharField("Numero de telephone *",max_length=120,help_text="Numero de telephone *")
    etabl_email_gnrl = models.EmailField("Adresse email Generale *",max_length=254,help_text="Adresse email Generale *",unique=True)
    etabl_site_internet = models.CharField("Site Internet ",max_length=254,help_text="Site Internet ")
    etabl_pays_situe = models.CharField(
        verbose_name="Pays *",
        max_length=100,
        help_text = "Pays *",
        choices = pays_tuple
    )
    etabl_list_associ = models.TextField("Enumeration des associations membres *",help_text="Enumerer la liste des associations d'universites ou d'etablissements superieurs dont votre etablissements est membre *")
    etabl_partenariat_inter = models.TextField("Enumeration partenariats internationaux *",help_text="Enumerer la liste des principaux partenariats internationaux *")
    #Informations sur l'etablissement

    #Informations sur le plus haut responsable
    res_etabl_nom = models.CharField("Nom du plus haut responsable *",max_length=70,help_text="Nom du plus haut responsable *")
    res_etabl_prenom = models.CharField("Prenom du plus haut responsable *",max_length=70,help_text="Prenom du plus haut responsable *")
    res_etabl_fonction = models.CharField("Fonction *",max_length=5,help_text="Fonction *",choices=fct_res_etabl)
    res_etabl_autre_fct_precis = models.CharField("Preciser si autre fonction",max_length=100,help_text="Preciser si autre fonction")
    res_etabl_numero_telephone_direct = models.CharField("Numero de telephone direct",max_length=15,help_text="Numero de telephone direct")
    res_etabl_email_direct = models.EmailField("Adresse email Direct *",max_length=254,help_text="Adresse email Direct *",unique=True)
    #Informations sur le plus haut responsable

    #Informations sur le Correspondant de la CIEC
    corr_ciec_sexe = models.CharField("Sexe du Correspondant CIEC *",max_length=5,help_text="Sexe du Correspondant CIEC *",choices=sexe_choices)
    corr_ciec_nom = models.CharField("Nom Correspondant *",max_length=100,help_text="Nom Correspondant *")
    corr_ciec_prenom = models.CharField("Prenom Correspondant *",max_length=100,help_text="Prenom Correspondant *")
    corr_ciec_fonction = models.CharField("Fonction au sein de l'etablissement *",max_length=100,help_text="Fonction au sein de l'etablissement *")
    corr_ciec_numero_telephone_direct = models.CharField("Numero de telephone direct",max_length=15,help_text="Numero de telephone direct")
    corr_ciec_email_direct = models.EmailField("Adresse email Direct *",max_length=254,help_text="Adresse email Direct *",unique=True)
    #Informations sur le Correspondant de la CIEC

    #Informations sur les elements synthetiques
    el_sync_nbr_etud_1_cy = models.FloatField("Nombre d'etudiant en premier Cycle *",help_text="Nombre d'etudiant en premier Cycle *")
    el_sync_nbr_etud_2_cy = models.FloatField("Nombre d'etudiant en deuxieme Cycle *",help_text="Nombre d'etudiant en deuxieme Cycle *")
    el_sync_nbr_etud_3_cy = models.FloatField("Nombre d'etudiant en troisieme Cycle *",help_text="Nombre d'etudiant en troisieme Cycle *")
    el_sync_nbr_prof_tit = models.FloatField("Nombre de professeurs titulaires *",help_text="Nombre de professeurs titulaires *")
    el_sync_nbr_prof_tit_with_doctorat = models.FloatField("Dont titiulaires d'un doctorat *",help_text="Dont titiulaires d'un doctorat *")
    el_sync_nbr_prof_vacat = models.FloatField("Nombre de professeurs titulaires *",help_text="Nombre de professeurs titulaires *")
    el_sync_nbr_prof_vacat_with_doctorat = models.FloatField("Dont titiulaires d'un doctorat *",help_text="Dont titiulaires d'un doctorat *")
    el_sync_nbr_labo_equip = models.FloatField("Nombre de laboratoires/equipes de recherche constituees *",help_text="Nombre de laboratoires/equipes de recherche constituees *")
    el_sync_dt_por_etud_cari = models.FloatField("Dont portant sur les etudes caribeennes *",help_text="Dont portant sur les etudes caribeennes *")
    el_sync_nbr_public_sc = models.FloatField("Nombre de publications scientifiques en 2015-2016 *",help_text="Nombre de publications scientifiques en 2015-2016 *")
    el_sync_dt_por_etud_cari_pub_sc = models.FloatField("Dont portant sur les etudes caribeennes *",help_text="Dont portant sur les etudes caribeennes *")
    el_sync_nbr_public_sc = models.FloatField("Nombre de these soutenues en 2015-2016 *",help_text="Nombre de these soutenues en 2015-2016 *")
    el_sync_dt_por_etud_cari_theses_s = models.FloatField("Dont portant sur les etudes caribeennes *",help_text="Dont portant sur les etudes caribeennes *")
    el_sync_langue_princi = models.CharField("Langue principale de travail",max_length=5,choices=langue_choices,help_text="Langue principale de travail")
    el_sync_autre_langue_prin = models.CharField("Autre langue a Preciser",max_length=50,help_text="Autre langue a Preciser")
    el_sync_langue_aut = models.CharField("Autres langues",max_length=5,choices=langue_choices,help_text="Autres langues")

    #Informations sur les elements synthetiques

    #Informations sur les activites de formations et de recherche sur les etudes caribeennes
    frec_indique = models.TextField("Indiquer tous les centre d'etudes,chaires,laboratoires,instituts,programmes de maitrise et de doctorat de votre universite specifiquement consacres aux problematiques caribeennes",help_text="Indiquer tous les centre d'etudes,chaires,laboratoires,instituts,programmes de maitrise et de doctorat de votre universite specifiquement consacres aux problematiques caribeennes")
    frec_attente = models.TextField("Quelles sont vos attentes vis a vis de la Chaire d'etudes caribeennes",help_text="Quelles sont vos attentes vis a vis de la Chaire d'etudes caribeennes")
    frec_contribution = models.TextField("Quelles peuvents etre vos contributions scientifiques, en ressources humaines, en expertise ou financieres a la Chaire d'etudes Caribeennes",help_text="Quelles peuvents etre vos contributions scientifiques, en ressources humaines, en expertise ou financieres a la Chaire d'etudes Caribeennes")
    #Informations sur les activites de formations et de recherche sur les etudes caribeennes

    #Informations sur les annexes obligatoires
    ann_creation = models.FileField(upload_to=user_directory_path,help_text="Texte creant l'etablissement *")
    ann_recon_off = models.FileField(upload_to=user_directory_path,help_text="Reconnaissance Officielle *")
    ann_list = models.FileField(upload_to=user_directory_path,help_text="Liste des facultes, departements, instituts et diplomes delivres pour chacun d'eux *")
    #Informations sur les annexes obligatoires
    show = models.CharField("A afficher publiquement",max_length=3,choices=(
        ('1','Visible sur le Site'),
        ('0','Invisible sur le Site'),
    ),default=0)
