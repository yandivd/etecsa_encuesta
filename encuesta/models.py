from django.db import models
from datetime import datetime

class Area_Organizativa(models.Model):
    nombre=models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre

class Encuesta(models.Model):

    MuyBien = 'MB'
    Bien = 'B'
    Regular = 'R'
    Mal = 'M'
    MuyMal= 'MM'
    Yes='S'
    No='N'

    DT='DT'
    CTA='CTA'
    T='T'
    TT='TT'
    ALSC='ALSC'
    UO='UO'

    LIMPIEZA_CHOICES = (
        (MuyBien, 'Muy Bien'),
        (Bien, 'Bien'),
        (Regular, 'Regular'),
        (Mal, 'Mal'),
        (MuyMal, 'Muy Mal'),
    )

    YES_NO_CHOICES = (
        (Yes, 'Si'),
        (No, 'No')
    )

    area= models.ForeignKey(Area_Organizativa, on_delete=models.CASCADE)
    #area=models.CharField(max_length=50, choices=AREA_ORGANIZATIVA_CHOICE)

    limpieza_val = models.CharField(max_length=50, choices=LIMPIEZA_CHOICES, default=MuyBien)

    sac_polvo=models.CharField(max_length=50, choices=YES_NO_CHOICES, default=MuyBien)

    limpieza_bannos=models.CharField(max_length=50, choices=LIMPIEZA_CHOICES, default=MuyBien)

    servicio_limpieza=models.CharField(max_length=50, choices=LIMPIEZA_CHOICES, default=MuyBien)

    fecha_hora=models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return str(id)


