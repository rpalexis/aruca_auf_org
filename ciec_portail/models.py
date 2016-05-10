from django.db import models
from auf.django.references.models import Pays
# Create your models here.

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
    # IMP Methode
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'pdf_files/user_{0}/{1}'.format(instance.user.id, filename)

    statut_candidatures = models.CharField("Statut de la Candidature",max_length=10,help_text ="Statut de la Candidature",choices=statut_choices)
    sexe = models.CharField("Genre du Candidat",max_length=10,help_text="Genre du Candidat",choices = sexe_choices)
    nom = models.CharField("Nom du Candidat",max_length=50,help_text="Nom du Candidat")
    prenom = models.CharField("Prenom du Candidat",max_length=50,help_text="Prenom du Candidat")
    date_naissance = models.DateField("Date de Naissance",auto_now=True,help_text="Date de Naissance")
    pays_nationalite = models.ForeignKey(
        Pays,
        on_delete=models.CASCADE,
        verbose_name="Pays de Nationnalite",
        related_name="nation_pays",
        help_text = "Pays de Nationnalite"
        ,db_index=True
    )
    adresse_residence = models.CharField("Adresse de residence du Candidat",max_length=100,help_text="Adresse de residence du Candidat")
    ville_residence = models.CharField("Ville de residence du Candidat",max_length=100,help_text="Ville de residence du Candidat")
    # pays_residence = models.ForeignKey(
    #     Pays,
    #     on_delete=models.CASCADE,
    #     verbose_name="Pays de Residence",
    #     related_name="nation_residence",
    #     db_index=True
    # )
    numero_telephone_direct = models.CharField("Numero de telephone direct",max_length=15,help_text="Numero de telephone direct")
    mail_direct = models.EmailField("Adresse email direct",max_length=254,help_text="Adresse email direct")
    etablissement_universitaire_1 = models.CharField("Etablissement Universitaire de Rattachement",max_length=100,help_text="Etablissement Universitaire de Rattachement")
    etabliseement_universitaire_autres = models.CharField("Autres Etablissement Universitaire a intervention reguliere",max_length=254,help_text="Autres Etablissement Universitaire a intervention reguliere")
    discipline_scient_gnrl = models.CharField("Discipline Scientifiques Generales",max_length=10,help_text="Discipline Scientifiques Generales")
    fonction_academique_now = models.CharField("Fonctions academiques actuellement exercees",max_length=100,help_text="Fonctions academiques actuellement exercees")
    fonction_academique_autre = models.CharField("Autres fonctions academiques actuellement exercees",max_length=100,help_text="Autres fonctions academiques actuellement exercees")
    pls_haut_diplome = models.CharField("Plus haut diplome obtenu",max_length=10,choices=diplome_obt_choices,help_text="Plus haut diplome obtenu")
    annee_obt = models.CharField("Annee d'obtention",max_length=5,help_text="Annee d'obtention")
    langue_travail_prin = models.CharField("Langue principale de travail",max_length=5,choices=langue_choices,help_text="Langue principale de travail")
    autre_langue_prin = models.CharField("Autre langue principale",max_length=50,help_text="Autre langue principale")
    langue_maitrise = models.CharField("Autres langues maitrise",max_length=5,choices=langue_choices_autres,help_text="Autres langues maitrise")
    autre_langue_maitrise = models.CharField("Autre autres langues maitrise",max_length=50,help_text="Autre autres langues maitrise")
    implication_academique = models.TextField("Implication Academique",help_text="Implication Academique")
    synthese_principale = models.TextField("Synthese Principale",help_text="Synthese Principale")
    ambition_pr_ciec = models.TextField("Ambition pour la CIEC",help_text="Synthese Principale")
    avantage_comparatif = models.TextField("Avantages Comparatifs",help_text="Synthese Principale")
    cv_detaille = models.FileField(upload_to=user_directory_path,help_text="Telecharger votre CV")
    lettre_soutien = models.FileField(upload_to=user_directory_path,help_text="Telecharger votre lettre de soutien")
    mise_disposition_legale = models.FileField(upload_to=user_directory_path,help_text="Telecharger votre mise en disposition")

    # Common attribute
    show = models.CharField("A afficher publiquement",max_length=3,choices=(
        ('1','Visible sur le Site'),
        ('0','Invisible sur le Site'),
    ))
