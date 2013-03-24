from django.contrib import admin

import models

admin.site.register(models.Persona)
admin.site.register(models.TipoExamen)
admin.site.register(models.CampoExamen)
admin.site.register(models.ResultadoExamen)
admin.site.register(models.ResultadoCampoExamen)