# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CampoExamen.unidad'
        db.alter_column(u'historias_medicas_campoexamen', 'unidad', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'TipoExamen.nombre'
        db.alter_column(u'historias_medicas_tipoexamen', 'nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25))

        # Changing field 'ResultadoCampoExamen.valor'
        db.alter_column(u'historias_medicas_resultadocampoexamen', 'valor', self.gf('django.db.models.fields.CharField')(max_length=25))

    def backwards(self, orm):

        # Changing field 'CampoExamen.unidad'
        db.alter_column(u'historias_medicas_campoexamen', 'unidad', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'TipoExamen.nombre'
        db.alter_column(u'historias_medicas_tipoexamen', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True))

        # Changing field 'ResultadoCampoExamen.valor'
        db.alter_column(u'historias_medicas_resultadocampoexamen', 'valor', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'historias_medicas.campoexamen': {
            'Meta': {'object_name': 'CampoExamen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'tipo_datos': ('django.db.models.fields.CharField', [], {'default': "'string'", 'max_length': '15'}),
            'tipo_examen': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campos'", 'to': u"orm['historias_medicas.TipoExamen']"}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        u'historias_medicas.historia': {
            'Meta': {'object_name': 'Historia'},
            'diagnostico': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.TextField', [], {}),
            'pendiente': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'historias'", 'null': 'True', 'to': u"orm['historias_medicas.Persona']"}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'pulso': ('django.db.models.fields.IntegerField', [], {}),
            'talla': ('django.db.models.fields.IntegerField', [], {}),
            'tension': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tratamiento': ('django.db.models.fields.TextField', [], {})
        },
        u'historias_medicas.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'historias_medicas.resultadocampoexamen': {
            'Meta': {'object_name': 'ResultadoCampoExamen'},
            'campo_examen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_medicas.CampoExamen']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.TextField', [], {}),
            'resultado_examen': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campos'", 'to': u"orm['historias_medicas.ResultadoExamen']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'historias_medicas.resultadoexamen': {
            'Meta': {'object_name': 'ResultadoExamen'},
            'historia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'examenes'", 'to': u"orm['historias_medicas.Historia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_examen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_medicas.TipoExamen']"})
        },
        u'historias_medicas.tipoexamen': {
            'Meta': {'object_name': 'TipoExamen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        }
    }

    complete_apps = ['historias_medicas']