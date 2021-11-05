from django.contrib import admin
from .models import Encuesta

# Register your models here.
class EncuestaAdmin(admin.ModelAdmin):
    list_display=('area','limpieza_val', 'sac_polvo', 'limpieza_bannos', 'servicio_limpieza')
    list_filter=('area','limpieza_val', 'sac_polvo', 'limpieza_bannos', 'servicio_limpieza',)

admin.site.register(Encuesta, EncuestaAdmin)
