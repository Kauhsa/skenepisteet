# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ScenePointEvent.accepted'
        db.add_column('skenepisteet_scenepointevent', 'accepted', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ScenePointEvent.accepted'
        db.delete_column('skenepisteet_scenepointevent', 'accepted')


    models = {
        'skenepisteet.pointsuggestion': {
            'Meta': {'object_name': 'PointSuggestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'scener': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skenepisteet.Scener']"})
        },
        'skenepisteet.scenepointevent': {
            'Meta': {'object_name': 'ScenePointEvent'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'award_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'scener': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skenepisteet.Scener']"})
        },
        'skenepisteet.scener': {
            'Meta': {'object_name': 'Scener'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['skenepisteet']
