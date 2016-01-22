# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chercheur'
        db.create_table('annuaire_chercheur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('langue', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('etablissement', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('etablissement_autre_nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('etablissement_autre_pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='etablissement_autre_pays', db_column='etablissement_autre_pays', to_field='code', to=orm['references.Pays'], blank=True, null=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('courriel', self.gf('django.db.models.fields.EmailField')(max_length=128, null=True, blank=True)),
            ('afficher_courriel', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('telecopie', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('mots_cles', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('diplome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('enseignement', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('problematique', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('equipement', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('laboratoire', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('terrain', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('discipline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('theme_recherche', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('partenaires', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('doctorants', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('stagiaire', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('publicationsInternational', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('publicationsAutre', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('publicationsColloc', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('communication', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('equipe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('domaine', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('annuaire', ['Chercheur'])

        # Adding model 'These'
        db.create_table('annuaire_these', (
            ('chercheur', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['annuaire.Chercheur'], unique=True, primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('annee', self.gf('django.db.models.fields.IntegerField')()),
            ('directeur', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('etablissement', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nb_pages', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('annuaire', ['These'])

        # Adding model 'PublicationsMajeur'
        db.create_table('annuaire_publicationsmajeur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chercheur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publications', to=orm['annuaire.Chercheur'])),
            ('auteurs', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('revue', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('annee', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nb_pages', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('annuaire', ['PublicationsMajeur'])


    def backwards(self, orm):
        # Deleting model 'Chercheur'
        db.delete_table('annuaire_chercheur')

        # Deleting model 'These'
        db.delete_table('annuaire_these')

        # Deleting model 'PublicationsMajeur'
        db.delete_table('annuaire_publicationsmajeur')


    models = {
        'annuaire.chercheur': {
            'Meta': {'ordering': "['nom', 'prenom', 'langue']", 'object_name': 'Chercheur'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'afficher_courriel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'communication': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'courriel': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diplome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'discipline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'doctorants': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'domaine': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'enseignement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'equipement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'etablissement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'etablissement_autre_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'etablissement_autre_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'etablissement_autre_pays'", 'db_column': "'etablissement_autre_pays'", 'to_field': "'code'", 'to': "orm['references.Pays']", 'blank': 'True', 'null': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laboratoire': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'langue': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'mots_cles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'partenaires': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'problematique': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publicationsAutre': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'publicationsColloc': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'publicationsInternational': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stagiaire': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'telecopie': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'terrain': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'theme_recherche': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'annuaire.publicationsmajeur': {
            'Meta': {'object_name': 'PublicationsMajeur'},
            'annee': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'auteurs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chercheur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publications'", 'to': "orm['annuaire.Chercheur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb_pages': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'revue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'annuaire.these': {
            'Meta': {'object_name': 'These'},
            'annee': ('django.db.models.fields.IntegerField', [], {}),
            'chercheur': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['annuaire.Chercheur']", 'unique': 'True', 'primary_key': 'True'}),
            'directeur': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'etablissement': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nb_pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'references.bureau': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Bureau', 'db_table': "u'ref_bureau'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Implantation']", 'db_column': "'implantation'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Region']", 'db_column': "'region'"})
        },
        'references.implantation': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Implantation', 'db_table': "u'ref_implantation'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse_physique_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_physique_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_physique'", 'to_field': "'code'", 'db_column': "'adresse_physique_pays'", 'to': "orm['references.Pays']"}),
            'adresse_physique_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'adresse_postale_boite_postale': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_postale_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_postale'", 'to_field': "'code'", 'db_column': "'adresse_postale_pays'", 'to': "orm['references.Pays']"}),
            'adresse_postale_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_rattachement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Implantation']", 'db_column': "'bureau_rattachement'"}),
            'code_meteo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'courriel': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'courriel_interne': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'date_extension': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fermeture': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_inauguration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_ouverture': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fax_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fuseau_horaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hebergement_convention': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hebergement_convention_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hebergement_etablissement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modif_date': ('django.db.models.fields.DateField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Region']", 'db_column': "'region'"}),
            'remarque': ('django.db.models.fields.TextField', [], {}),
            'responsable_implantation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'statut': ('django.db.models.fields.IntegerField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telephone_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'references.pays': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Pays', 'db_table': "u'ref_pays'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Bureau']", 'to_field': "'code'", 'null': 'True', 'db_column': "'code_bureau'", 'blank': 'True'}),
            'code_iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'developpement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monnaie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nord_sud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Region']", 'db_column': "'region'"})
        },
        'references.region': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Region', 'db_table': "u'ref_region'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation_bureau': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gere_region'", 'null': 'True', 'db_column': "'implantation_bureau'", 'to': "orm['references.Implantation']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['annuaire']