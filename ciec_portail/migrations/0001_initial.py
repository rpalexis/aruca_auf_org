# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ciec_portail.models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceCandidature',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('statut_candidatures', models.CharField(help_text='Statut de la Candidature', choices=[('MCA', "Membre du Conseil d'Administration"), ('MCAD', 'Membre du Conseil Academique'), ('CG', 'Coordonateur General')], max_length=10, verbose_name='Statut de la Candidature')),
                ('sexe', models.CharField(help_text='Genre du Candidat', choices=[('h', 'Homme'), ('f', 'Femme')], max_length=10, verbose_name='Genre du Candidat')),
                ('nom', models.CharField(help_text='Nom du Candidat', max_length=50, verbose_name='Nom du Candidat')),
                ('prenom', models.CharField(help_text='Prenom du Candidat', max_length=50, verbose_name='Prenom du Candidat')),
                ('date_naissance', models.DateField(help_text='Date de Naissance', auto_now=True, verbose_name='Date de Naissance')),
                ('adresse_residence', models.CharField(help_text='Adresse de residence du Candidat', max_length=100, verbose_name='Adresse de residence du Candidat')),
                ('ville_residence', models.CharField(help_text='Ville de residence du Candidat', max_length=100, verbose_name='Ville de residence du Candidat')),
                ('numero_telephone_direct', models.CharField(help_text='Numero de telephone direct', max_length=15, verbose_name='Numero de telephone direct')),
                ('mail_direct', models.EmailField(help_text='Adresse email direct', max_length=254, verbose_name='Adresse email direct')),
                ('etablissement_universitaire_1', models.CharField(help_text='Etablissement Universitaire de Rattachement', max_length=100, verbose_name='Etablissement Universitaire de Rattachement')),
                ('etabliseement_universitaire_autres', models.CharField(help_text='Autres Etablissement Universitaire a intervention reguliere', max_length=254, verbose_name='Autres Etablissement Universitaire a intervention reguliere')),
                ('discipline_scient_gnrl', models.CharField(help_text='Discipline Scientifiques Generales', max_length=10, verbose_name='Discipline Scientifiques Generales')),
                ('fonction_academique_now', models.CharField(max_length=100, verbose_name='Fonctions academiques actuellement exercees')),
                ('fonction_academique_autre', models.CharField(max_length=100, verbose_name='Autres fonctions academiques actuellement exercees')),
                ('pls_haut_diplome', models.CharField(choices=[('LC', 'Licence ou equivalent'), ('MS', 'Master'), ('DT', 'Doctorat')], max_length=10, verbose_name='Plus haut diplome obtenu')),
                ('annee_obt', models.CharField(max_length=5, verbose_name="Annee d'obtention")),
                ('langue_travail_prin', models.CharField(choices=[('FR', 'Francais'), ('EN', 'Anglais'), ('ES', 'Espagnol'), ('CR', 'Creole')], max_length=5, verbose_name='Langue principale de travail')),
                ('autre_langue_prin', models.CharField(max_length=50, verbose_name='Autre langue principale')),
                ('langue_maitrise', models.CharField(choices=[('NOP', "Pas d'autres"), ('FR', 'Francais'), ('EN', 'Anglais'), ('ES', 'Espagnol'), ('CR', 'Creole')], max_length=5, verbose_name='Autres langues maitrise')),
                ('autre_langue_maitrise', models.CharField(max_length=50, verbose_name='Autre autres langues maitrise')),
                ('implication_academique', models.TextField(verbose_name='Implication Academique')),
                ('synthese_principale', models.TextField(verbose_name='Synthese Principale')),
                ('ambition_pr_ciec', models.TextField(verbose_name='Ambition pour la CIEC')),
                ('avantage_comparatif', models.TextField(verbose_name='Avantages Comparatifs')),
                ('cv_detaille', models.FileField(upload_to=ciec_portail.models.InstanceCandidature.user_directory_path)),
                ('lettre_soutien', models.FileField(upload_to=ciec_portail.models.InstanceCandidature.user_directory_path)),
                ('mise_disposition_legale', models.FileField(upload_to=ciec_portail.models.InstanceCandidature.user_directory_path)),
                ('show', models.CharField(choices=[('1', 'Visible sur le Site'), ('0', 'Invisible sur le Site')], max_length=3, verbose_name='A afficher publiquement')),
                ('pays_nationalite', models.ForeignKey(to='references.Pays', related_name='nation_pays', verbose_name='Pays de Nationnalite')),
                ('pays_residence', models.ForeignKey(to='references.Pays', related_name='nation_residence', verbose_name='Pays de Residence')),
            ],
        ),
    ]
