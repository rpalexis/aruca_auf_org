# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('photos_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('date_album', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('photos', ['Album'])

        # Adding model 'Photo'
        db.create_table('photos_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['photos.Album'])),
            ('legende', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('photos', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('photos_album')

        # Deleting model 'Photo'
        db.delete_table('photos_photo')


    models = {
        'photos.album': {
            'Meta': {'object_name': 'Album'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_album': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'texte': ('django.db.models.fields.TextField', [], {})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['photos.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'legende': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['photos']