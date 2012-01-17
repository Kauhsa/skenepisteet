# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Scener'
        db.create_table('skenepisteet_scener', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('skenepisteet', ['Scener'])

        # Adding model 'ScenePointEvent'
        db.create_table('skenepisteet_scenepointevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('award_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('scener', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skenepisteet.Scener'])),
        ))
        db.send_create_signal('skenepisteet', ['ScenePointEvent'])

        # Adding model 'PointSuggestion'
        db.create_table('skenepisteet_pointsuggestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scener', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skenepisteet.Scener'])),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('reason', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('skenepisteet', ['PointSuggestion'])


    def backwards(self, orm):
        
        # Deleting model 'Scener'
        db.delete_table('skenepisteet_scener')

        # Deleting model 'ScenePointEvent'
        db.delete_table('skenepisteet_scenepointevent')

        # Deleting model 'PointSuggestion'
        db.delete_table('skenepisteet_pointsuggestion')


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
