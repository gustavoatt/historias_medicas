# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Historia', fields ['persona']
        db.delete_unique('historias_medicas_historia', ['persona_id'])

        # Adding unique constraint on 'Historia', fields ['fecha']
        db.create_unique('historias_medicas_historia', ['fecha'])


        # Changing field 'Historia.peso'
        db.alter_column('historias_medicas_historia', 'peso', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

    def backwards(self, orm):
        # Removing unique constraint on 'Historia', fields ['fecha']
        db.delete_unique('historias_medicas_historia', ['fecha'])

        # Adding unique constraint on 'Historia', fields ['persona']
        db.create_unique('historias_medicas_historia', ['persona_id'])


        # Changing field 'Historia.peso'
        db.alter_column('historias_medicas_historia', 'peso', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'historias_medicas.historia': {
            'Meta': {'object_name': 'Historia'},
            'diagnostico': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'unique': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.TextField', [], {}),
            'pendiente': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'historias'", 'null': 'True', 'to': "orm['historias_medicas.Persona']"}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
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