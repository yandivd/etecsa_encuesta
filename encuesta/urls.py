from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="Home" ),
    path('telepunto/', views.telepunto, name="Telepunto"),
    path('muchas_gracias/', views.final, name="Final"),
    path('form_encuesta/', views.EncuestaCreateView.as_view(), name="Encuesta"),
    path('resultados/', views.Resumen, name='Resultados'),
    path('direccion_territorial/', views.ResumenDT, name='DT'),
    path('centro_telecomunicaciones/', views.ResumenCTA, name='CTA'),
    path('telepuntol/', views.ResumenT, name='T'),
    path('taller_telf/', views.ResumenTT, name='TT'),
    path('chalet/', views.ResumenALSC, name='ALSC'),
    path('unidad_operativa/', views.ResumenUO, name='UO'),


]