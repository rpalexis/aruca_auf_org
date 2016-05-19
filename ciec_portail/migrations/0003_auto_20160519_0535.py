# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ciec_portail.models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '__first__'),
        ('ciec_portail', '0002_remove_instancecandidature_pays_residence'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatMembre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('stt_canditat_membre', models.CharField(help_text='Statut de la Candidature *', verbose_name='Statut de la Candidature *', choices=[('MT', 'Membre Titulaire'), ('MO', 'Membre Observateur')], max_length=5)),
                ('etabl_nom', models.CharField(help_text="Nom de l'etablissement *", verbose_name="Nom de l'etablissement *", max_length=200)),
                ('etabl_sigle', models.CharField(help_text="Sigle de l'etablissement *", verbose_name="Sigle de l'etablissement *", max_length=100)),
                ('etabl_annee_creation', models.CharField(help_text='Annee de creation etablissement *', verbose_name='Annee de creation etablissement *', max_length=5)),
                ('etabl_statut_officiel', models.CharField(help_text='Statut Officiel *', verbose_name='Statut Officiel *', choices=[('EPu', 'Etablissement Public'), ('EPr', 'Etablissement Prive')], max_length=5)),
                ('etabl_adresse', models.CharField(help_text='Adresse *', verbose_name='Adresse *', max_length=100)),
                ('etabl_ville', models.CharField(help_text='Ville *', verbose_name='Ville *', max_length=100)),
                ('etabl_phone_number', models.CharField(help_text='Numero de telephone *', verbose_name='Numero de telephone *', max_length=120)),
                ('etabl_email_gnrl', models.EmailField(help_text='Adresse email Generale *', verbose_name='Adresse email Generale *', unique=True, max_length=254)),
                ('etabl_site_internet', models.CharField(help_text='Site Internet ', verbose_name='Site Internet ', max_length=254)),
                ('etabl_list_associ', models.TextField(help_text='Enumeration des associations membres *', verbose_name='Enumeration des associations membres *')),
                ('etabl_partenariat_inter', models.TextField(help_text='Enumeration partenariats internationaux *', verbose_name='Enumeration partenariats internationaux *')),
                ('res_etabl_nom', models.CharField(help_text='Nom du plus haut responsable *', verbose_name='Nom du plus haut responsable *', max_length=70)),
                ('res_etabl_prenom', models.CharField(help_text='Prenom du plus haut responsable *', verbose_name='Prenom du plus haut responsable *', max_length=70)),
                ('res_etabl_fonction', models.CharField(help_text='Fonction *', verbose_name='Fonction *', choices=[('RCT', 'Recteur'), ('DIR', 'Directeur')], max_length=5)),
                ('res_etabl_numero_telephone_direct', models.CharField(help_text='Numero de telephone direct', verbose_name='Numero de telephone direct', max_length=15)),
                ('res_etabl_email_direct', models.EmailField(help_text='Adresse email Direct *', verbose_name='Adresse email Direct *', unique=True, max_length=254)),
                ('corr_ciec_sexe', models.CharField(help_text='Sexe du Correspondant CIEC *', verbose_name='Sexe du Correspondant CIEC *', choices=[('h', 'Homme'), ('f', 'Femme')], max_length=5)),
                ('corr_ciec_nom', models.CharField(help_text='Nom Correspondant *', verbose_name='Nom Correspondant *', max_length=100)),
                ('corr_ciec_prenom', models.CharField(help_text='Prenom Correspondant *', verbose_name='Prenom Correspondant *', max_length=100)),
                ('corr_ciec_fonction', models.CharField(help_text="Fonction au sein de l'etablissement *", verbose_name="Fonction au sein de l'etablissement *", max_length=100)),
                ('corr_ciec_numero_telephone_direct', models.CharField(help_text='Numero de telephone direct', verbose_name='Numero de telephone direct', max_length=15)),
                ('corr_ciec_email_direct', models.EmailField(help_text='Adresse email Direct *', verbose_name='Adresse email Direct *', unique=True, max_length=254)),
                ('el_sync_nbr_etud_1_cy', models.FloatField(help_text="Nombre d'etudiant en premier Cycle *", verbose_name="Nombre d'etudiant en premier Cycle *")),
                ('el_sync_nbr_etud_2_cy', models.FloatField(help_text="Nombre d'etudiant en deuxieme Cycle *", verbose_name="Nombre d'etudiant en deuxieme Cycle *")),
                ('el_sync_nbr_etud_3_cy', models.FloatField(help_text="Nombre d'etudiant en troisieme Cycle *", verbose_name="Nombre d'etudiant en troisieme Cycle *")),
                ('el_sync_nbr_prof_tit', models.FloatField(help_text='Nombre de professeurs titulaires *', verbose_name='Nombre de professeurs titulaires *')),
                ('el_sync_nbr_prof_tit_with_doctorat', models.FloatField(help_text="Dont titiulaires d'un doctorat *", verbose_name="Dont titiulaires d'un doctorat *")),
                ('el_sync_nbr_prof_vacat', models.FloatField(help_text='Nombre de professeurs titulaires *', verbose_name='Nombre de professeurs titulaires *')),
                ('el_sync_nbr_prof_vacat_with_doctorat', models.FloatField(help_text="Dont titiulaires d'un doctorat *", verbose_name="Dont titiulaires d'un doctorat *")),
                ('el_sync_nbr_labo_equip', models.FloatField(help_text='Nombre de laboratoires/equipes de recherche constituees *', verbose_name='Nombre de laboratoires/equipes de recherche constituees *')),
                ('el_sync_dt_por_etud_cari', models.FloatField(help_text='Dont portant sur les etudes caribeennes *', verbose_name='Dont portant sur les etudes caribeennes *')),
                ('el_sync_dt_por_etud_cari_pub_sc', models.FloatField(help_text='Dont portant sur les etudes caribeennes *', verbose_name='Dont portant sur les etudes caribeennes *')),
                ('el_sync_nbr_public_sc', models.FloatField(help_text='Nombre de these soutenues en 2015-2016 *', verbose_name='Nombre de these soutenues en 2015-2016 *')),
                ('el_sync_dt_por_etud_cari_theses_s', models.FloatField(help_text='Dont portant sur les etudes caribeennes *', verbose_name='Dont portant sur les etudes caribeennes *')),
                ('el_sync_langue_princi', models.CharField(help_text='Langue principale de travail', verbose_name='Langue principale de travail', choices=[('FR', 'Francais'), ('EN', 'Anglais'), ('ES', 'Espagnol'), ('CR', 'Creole')], max_length=5)),
                ('el_sync_autre_langue_prin', models.CharField(help_text='Autre langue a Preciser', verbose_name='Autre langue a Preciser', max_length=50)),
                ('el_sync_langue_aut', models.CharField(help_text='Autres langues', verbose_name='Autres langues', choices=[('FR', 'Francais'), ('EN', 'Anglais'), ('ES', 'Espagnol'), ('CR', 'Creole')], max_length=5)),
                ('frec_indique', models.TextField(help_text="Indiquer tous les centre d'etudes,chaires,laboratoires,instituts,programmes de maitrise et de doctorat de votre universite specifiquement consacres aux problematiques caribeennes", verbose_name="Indiquer tous les centre d'etudes,chaires,laboratoires,instituts,programmes de maitrise et de doctorat de votre universite specifiquement consacres aux problematiques caribeennes")),
                ('frec_attente', models.TextField(help_text="Quelles sont vos attentes vis a vis de la Chaire d'etudes caribeennes", verbose_name="Quelles sont vos attentes vis a vis de la Chaire d'etudes caribeennes")),
                ('frec_contribution', models.TextField(help_text="Quelles peuvents etre vos contributions scientifiques, en ressources humaines, en expertise ou financieres a la Chaire d'etudes Caribeennes", verbose_name="Quelles peuvents etre vos contributions scientifiques, en ressources humaines, en expertise ou financieres a la Chaire d'etudes Caribeennes")),
                ('ann_creation', models.FileField(help_text="Texte creant l'etablissement *", upload_to=ciec_portail.models.CandidatMembre.user_directory_path)),
                ('ann_recon_off', models.FileField(help_text='Reconnaissance Officielle *', upload_to=ciec_portail.models.CandidatMembre.user_directory_path)),
                ('ann_list', models.FileField(help_text="Liste des facultes, departements, instituts et diplomes delivres pour chacun d'eux *", upload_to=ciec_portail.models.CandidatMembre.user_directory_path)),
                ('show', models.CharField(verbose_name='A afficher publiquement', default=0, choices=[('1', 'Visible sur le Site'), ('0', 'Invisible sur le Site')], max_length=3)),
                ('etabl_pays_situe', models.ForeignKey(related_name='nation_pays_cc', help_text='Pays *', to='references.Pays', verbose_name='Pays *')),
            ],
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='ambition_pr_ciec',
            field=models.TextField(help_text='Synthese Principale', verbose_name='Ambition pour la CIEC'),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='annee_obt',
            field=models.CharField(help_text="Annee d'obtention", verbose_name="Annee d'obtention", max_length=5),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='autre_langue_maitrise',
            field=models.CharField(help_text='Autre autres langues maitrise', verbose_name='Autre autres langues maitrise', max_length=50),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='autre_langue_prin',
            field=models.CharField(help_text='Autre langue principale', verbose_name='Autre langue principale', max_length=50),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='avantage_comparatif',
            field=models.TextField(help_text='Synthese Principale', verbose_name='Avantages Comparatifs'),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='cv_detaille',
            field=models.FileField(help_text='Telecharger votre CV', upload_to=ciec_portail.models.InstanceCandidature.user_directory_path),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='date_naissance',
            field=models.DateField(help_text='Date de Naissance', verbose_name='Date de Naissance'),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='fonction_academique_autre',
            field=models.CharField(help_text='Autres fonctions academiques actuellement exercees', verbose_name='Autres fonctions academiques actuellement exercees', max_length=100),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='fonction_academique_now',
            field=models.CharField(help_text='Fonctions academiques actuellement exercees', verbose_name='Fonctions academiques actuellement exercees', max_length=100),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='implication_academique',
            field=models.TextField(help_text='Implication Academique', verbose_name='Implication Academique'),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='langue_maitrise',
            field=models.CharField(help_text='Autres langues maitrise', verbose_name='Autres langues maitrise', choices=[('NOP', "Pas d'autres"), ('FR', 'Francais'), ('EN', 'Anglais'), ('ES', 'Espagnol'), ('CR', 'Creole')], max_length=5),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='langue_travail_prin',
            field=models.CharField(help_text='Langue principale de travail', verbose_name='Langue principale de travail', choices=[('FR', 'Francais'), ('EN', 'Anglais'), ('ES', 'Espagnol'), ('CR', 'Creole')], max_length=5),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='lettre_soutien',
            field=models.FileField(help_text='Telecharger votre lettre de soutien', upload_to=ciec_portail.models.InstanceCandidature.user_directory_path),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='mail_direct',
            field=models.EmailField(help_text='Adresse email direct', verbose_name='Adresse email direct', unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='mise_disposition_legale',
            field=models.FileField(help_text='Telecharger votre mise en disposition', upload_to=ciec_portail.models.InstanceCandidature.user_directory_path),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='pays_nationalite',
            field=models.ForeignKey(related_name='nation_pays', help_text='Pays de Nationnalite', to='references.Pays', verbose_name='Pays de Nationnalite'),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='pls_haut_diplome',
            field=models.CharField(help_text='Plus haut diplome obtenu', verbose_name='Plus haut diplome obtenu', choices=[('LC', 'Licence ou equivalent'), ('MS', 'Master'), ('DT', 'Doctorat')], max_length=10),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='show',
            field=models.CharField(verbose_name='A afficher publiquement', default=0, choices=[('1', 'Visible sur le Site'), ('0', 'Invisible sur le Site')], max_length=3),
        ),
        migrations.AlterField(
            model_name='instancecandidature',
            name='synthese_principale',
            field=models.TextField(help_text='Synthese Principale', verbose_name='Synthese Principale'),
        ),
    ]
