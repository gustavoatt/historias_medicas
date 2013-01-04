# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table('historias_medicas_persona', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cedula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('direccion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('telefono_casa', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('telefono_celular', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('historias_medicas', ['Persona'])

        # Adding model 'Historia'
        db.create_table('historias_medicas_historia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('motivo', self.gf('django.db.models.fields.TextField')()),
            ('peso', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('talla', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('tension', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('pulso', self.gf('django.db.models.fields.IntegerField')()),
            ('diagnostico', self.gf('django.db.models.fields.TextField')()),
            ('tratamiento', self.gf('django.db.models.fields.TextField')()),
            ('pendiente', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('historias_medicas', ['Historia'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table('historias_medicas_persona')

        # Deleting model 'Historia'
        db.delete_table('historias_medicas_historia')


    models = {
        'historias_medicas.historia': {
            'Meta': {'object_name': 'Historia'},
            'diagnostico': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.TextField', [], {}),
            'pendiente': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'peso': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'pulso': ('django.db.models.fields.IntegerField', [], {}),
            'talla': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'tension': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tratamiento': ('django.db.models.fields.TextField', [], {})
        },
        'historias_medicas.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['historias_medicas']