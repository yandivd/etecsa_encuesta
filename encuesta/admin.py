from django.contrib import admin
from .models import Encuesta, Area_Organizativa

# Register your models here.
class EncuestaAdmin(admin.ModelAdmin):
    list_display=('fecha_hora','area','limpieza_val', 'sac_polvo', 'limpieza_bannos', 'servicio_limpieza')
    list_filter=('fecha_hora','area','limpieza_val', 'sac_polvo', 'limpieza_bannos', 'servicio_limpieza',)

class Area_OrganizativaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    list_filter=('nombre',)

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Area_Organizativa, Area_OrganizativaAdmin)