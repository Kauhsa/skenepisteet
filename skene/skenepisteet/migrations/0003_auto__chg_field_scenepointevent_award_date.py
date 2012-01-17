# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ScenePointEvent.award_date'
        db.alter_column('skenepisteet_scenepointevent', 'award_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Changing field 'ScenePointEvent.award_date'
        db.alter_column('skenepisteet_scenepointevent', 'award_date', self.gf('django.db.models.fields.DateTimeField')())


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
            'award_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 17, 21, 4, 43, 682000)', 'auto_now_add': 'True', 'blank': 'True'}),
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
