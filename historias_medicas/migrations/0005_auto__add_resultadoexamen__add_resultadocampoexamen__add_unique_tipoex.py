# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResultadoExamen'
        db.create_table('historias_medicas_resultadoexamen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('historia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='examenes', to=orm['historias_medicas.Historia'])),
            ('tipo_examen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historias_medicas.TipoExamen'])),
        ))
        db.send_create_signal('historias_medicas', ['ResultadoExamen'])

        # Adding model 'ResultadoCampoExamen'
        db.create_table('historias_medicas_resultadocampoexamen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resultado_examen', self.gf('django.db.models.fields.related.ForeignKey')(related_name='campos', to=orm['historias_medicas.ResultadoExamen'])),
            ('campo_examen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historias_medicas.CampoExamen'])),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nota', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('historias_medicas', ['ResultadoCampoExamen'])

        # Adding unique constraint on 'TipoExamen', fields ['nombre']
        db.create_unique('historias_medicas_tipoexamen', ['nombre'])

        # Adding field 'CampoExamen.unidad'
        db.add_column('historias_medicas_campoexamen', 'unidad',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'TipoExamen', fields ['nombre']
        db.delete_unique('historias_medicas_tipoexamen', ['nombre'])

        # Deleting model 'ResultadoExamen'
        db.delete_table('historias_medicas_resultadoexamen')

        # Deleting model 'ResultadoCampoExamen'
        db.delete_table('historias_medicas_resultadocampoexamen')

        # Deleting field 'CampoExamen.unidad'
        db.delete_column('historias_medicas_campoexamen', 'unidad')


    models = {
        'historias_medicas.campoexamen': {
            'Meta': {'object_name': 'CampoExamen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'tipo_datos': ('django.db.models.fields.CharField', [], {'default': "'string'", 'max_length': '15'}),
            'tipo_examen': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campos'", 'to': "orm['historias_medicas.TipoExamen']"}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        'historias_medicas.historia': {
            'Meta': {'object_name': 'Historia'},
            'diagnostico': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'unique': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.TextField', [], {}),
            'pendiente': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'historias'", 'null': 'True', 'to': "orm['historias_medicas.Persona']"}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'pulso': ('django.db.models.fields.IntegerField', [], {}),
            'talla': ('django.db.models.fields.IntegerField', [], {}),
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
        },
        'historias_medicas.resultadocampoexamen': {
            'Meta': {'object_name': 'ResultadoCampoExamen'},
            'campo_examen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['historias_medicas.CampoExamen']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.TextField', [], {}),
            'resultado_examen': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campos'", 'to': "orm['historias_medicas.ResultadoExamen']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'historias_medicas.resultadoexamen': {
            'Meta': {'object_name': 'ResultadoExamen'},
            'historia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'examenes'", 'to': "orm['historias_medicas.Historia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_examen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['historias_medicas.TipoExamen']"})
        },
        'historias_medicas.tipoexamen': {
            'Meta': {'object_name': 'TipoExamen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['historias_medicas']