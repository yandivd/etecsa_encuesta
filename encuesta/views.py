from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Encuesta
from .forms import EncuestasForm
from django.urls import reverse_lazy
import matplotlib.pyplot as plt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def telepunto(request):
    return render(request, 'telepunto.html')

def final(request):
    return render(request, 'gracias.html')

class EncuestaCreateView(CreateView):
    model=Encuesta
    form_class=EncuestasForm
    template_name='formulario.html'
    success_url=reverse_lazy('Final')

def ResumenDT(request):
    encuestasDT=Encuesta.objects.filter(area__exact='DT')
    ###Direccion Territorial###
    DTcantMB=0
    DTcantB=0
    DTcantR=0
    DTcantM=0
    DTcantMM=0
    

##Direccion Territorial
    for i in encuestasDT:
        if i.servicio_limpieza=='MB':
            DTcantMB+=1
        elif i.servicio_limpieza=='B':
            DTcantB+=1
        elif i.servicio_limpieza=='R':
            DTcantR+=1
        elif i.servicio_limpieza=='M':
            DTcantM+=1
        elif i.servicio_limpieza=='MM':
            DTcantMM+=1

####Metodo para calcular porciento
    total=encuestasDT.count()
    #porciento MB
    porcMB=(DTcantMB*100)/total

    #porciento B
    porcB=(DTcantB*100)/total

    #porciento R
    porcR=(DTcantR*100)/total

    #porciento M
    porcM=(DTcantM*100)/total

    #porciento MM
    porcMM=(DTcantMM*100)/total
    ###GRAFICANDO#####
    calif=['MB','B','R','M','MM']
    cant=[DTcantMB, DTcantB, DTcantR, DTcantM, DTcantMM]
    colores = ['lightgreen','yellow','#FFA500','red','sienna']
    desface=(0.1,0,0,0,0)
    plt.pie(cant, labels=calif, colors=colores,autopct='%1.2f%%', explode=desface)
    plt.title('Direccion Territorial')


    data={ 
            "DTcantMB":DTcantMB,
            "DTcantB":DTcantB,
            "DTcantR": DTcantR,
            "DTcantM":DTcantM,
            "DTcantMM": DTcantMM,
            "porcMB": porcMB,
            "porcB": porcB,
            "porcR": porcR,
            "porcM": porcM,
            "porcMM": porcMM,
            "show": plt.savefig('encuesta/static/encuesta/GDT.png'),
            "del": plt.close()
    }

    return render(request, 'dt.html',data)

def ResumenCTA(request):
    encuestasCTA=Encuesta.objects.filter(area__exact='CTA')
    ###Centro Telefonico Artemisa###
    CTAcantMB=0
    CTAcantB=0
    CTAcantR=0
    CTAcantM=0
    CTAcantMM=0

##Centro de Telecomunicaciones Artemisa
    for i in encuestasCTA:
        if i.servicio_limpieza=='MB':
            CTAcantMB+=1
        elif i.servicio_limpieza=='B':
            CTAcantB+=1
        elif i.servicio_limpieza=='R':
            CTAcantR+=1
        elif i.servicio_limpieza=='M':
            CTAcantM+=1
        elif i.servicio_limpieza=='MM':
            CTAcantMM+=1

####Metodo para calcular porciento
    total=encuestasCTA.count()
    #porciento MB
    porcMB=(CTAcantMB*100)/total

    #porciento B
    porcB=(CTAcantB*100)/total

    #porciento R
    porcR=(CTAcantR*100)/total

    #porciento M
    porcM=(CTAcantM*100)/total

    #porciento MM
    porcMM=(CTAcantMM*100)/total

        ###GRAFICANDO#####
    calif=['MB','B','R','M','MM']
    cant=[CTAcantMB, CTAcantB, CTAcantR, CTAcantM, CTAcantMM]
    colores = ['lightgreen','yellow','#FFA500','red','sienna']
    desface=(0.1,0,0,0,0)
    plt.pie(cant, labels=calif, colors=colores,autopct='%1.2f%%', explode=desface)
    plt.title('Centro de Telecomunicaciones Artemisa')

    data={

            "CTAcantMB":CTAcantMB,
            "CTAcantB":CTAcantB,
            "CTAcantR": CTAcantR,
            "CTAcantM":CTAcantM,
            "CTAcantMM": CTAcantMM,
            "porcMB": porcMB,
            "porcB": porcB,
            "porcR": porcR,
            "porcM": porcM,
            "porcMM": porcMM,
            "show": plt.savefig('encuesta/static/encuesta/GCTA.png'),
            "del": plt.close()
            }

    return render(request, 'cta.html', data)

def ResumenT(request):
    encuestasT=Encuesta.objects.filter(area__exact='T')
    ###Telepunto#
    TcantMB=0
    TcantB=0
    TcantR=0
    TcantM=0
    TcantMM=0

##Telepunto
    for i in encuestasT:
        if i.servicio_limpieza=='MB':
            TcantMB+=1
        elif i.servicio_limpieza=='B':
            TcantB+=1
        elif i.servicio_limpieza=='R':
            TcantR+=1
        elif i.servicio_limpieza=='M':
            TcantM+=1
        elif i.servicio_limpieza=='MM':
            TcantMM+=1

####Metodo para calcular porciento
    total=encuestasT.count()
    #porciento MB
    porcMB=(TcantMB*100)/total

    #porciento B
    porcB=(TcantB*100)/total

    #porciento R
    porcR=(TcantR*100)/total

    #porciento M
    porcM=(TcantM*100)/total

    #porciento MM
    porcMM=(TcantMM*100)/total

    calif=['MB','B','R','M','MM']
    cant=[TcantMB, TcantB, TcantR, TcantM, TcantMM]
    colores = ['lightgreen','yellow','#FFA500','red','sienna']
    desface=(0.1,0,0,0,0)
    plt.pie(cant, labels=calif, colors=colores,autopct='%1.2f%%', explode=desface)
    plt.title('Telepunto')

    data={

            "TcantMB":TcantMB,
            "TcantB":TcantB,
            "TcantR": TcantR,
            "TcantM":TcantM,
            "TcantMM": TcantMM,
            "porcMB": porcMB,
            "porcB": porcB,
            "porcR": porcR,
            "porcM": porcM,
            "porcMM": porcMM,
            "show": plt.savefig('encuesta/static/encuesta/GT.png'),
            "del": plt.close()
            }

    return render(request, 'tel.html', data)   

def ResumenTT(request):
    encuestasTT=Encuesta.objects.filter(area__exact='TT')
    ###Teller telefonos###
    TTcantMB=0
    TTcantB=0
    TTcantR=0
    TTcantM=0
    TTcantMM=0

##Taller telefonos
    for i in encuestasTT:
        if i.servicio_limpieza=='MB':
            TTcantMB+=1
        elif i.servicio_limpieza=='B':
            TTcantB+=1
        elif i.servicio_limpieza=='R':
            TTcantR+=1
        elif i.servicio_limpieza=='M':
            TTcantM+=1
        elif i.servicio_limpieza=='MM':
            TTcantMM+=1

####Metodo para calcular porciento
    total=encuestasTT.count()
    #porciento MB
    porcMB=(TTcantMB*100)/total

    #porciento B
    porcB=(TTcantB*100)/total

    #porciento R
    porcR=(TTcantR*100)/total

    #porciento M
    porcM=(TTcantM*100)/total

    #porciento MM
    porcMM=(TTcantMM*100)/total

    calif=['MB','B','R','M','MM']
    cant=[TTcantMB, TTcantB, TTcantR, TTcantM, TTcantMM]
    colores = ['lightgreen','yellow','#FFA500','red','sienna']
    desface=(0.1,0,0,0,0)
    plt.pie(cant, labels=calif, colors=colores,autopct='%1.2f%%', explode=desface)
    plt.title('Taller de Telefonos')

    data={

            "TTcantMB":TTcantMB,
            "TTcantB":TTcantB,
            "TTcantR": TTcantR,
            "TTcantM":TTcantM,
            "TTcantMM": TTcantMM,
            "porcMB": porcMB,
            "porcB": porcB,
            "porcR": porcR,
            "porcM": porcM,
            "porcMM": porcMM,
            "show": plt.savefig('encuesta/static/encuesta/GTT.png'),
            "del": plt.close()
            }

    return render(request, 'taller_telf.html', data)  

def ResumenALSC(request):
    encuestasALSC=Encuesta.objects.filter(area__exact='ALSC')
    ###Chalet###
    ALSCcantMB=0
    ALSCcantB=0
    ALSCcantR=0
    ALSCcantM=0
    ALSCcantMM=0

##Chalet
    for i in encuestasALSC:
        if i.servicio_limpieza=='MB':
            ALSCcantMB+=1
        elif i.servicio_limpieza=='B':
            ALSCcantB+=1
        elif i.servicio_limpieza=='R':
            ALSCcantR+=1
        elif i.servicio_limpieza=='M':
            ALSCcantM+=1
        elif i.servicio_limpieza=='MM':
            ALSCcantMM+=1

####Metodo para calcular porciento
    total=encuestasALSC.count()
    #porciento MB
    porcMB=(ALSCcantMB*100)/total

    #porciento B
    porcB=(ALSCcantB*100)/total

    #porciento R
    porcR=(ALSCcantR*100)/total

    #porciento M
    porcM=(ALSCcantM*100)/total

    #porciento MM
    porcMM=(ALSCcantMM*100)/total

    calif=['MB','B','R','M','MM']
    cant=[ALSCcantMB, ALSCcantB, ALSCcantR, ALSCcantM, ALSCcantMM]
    colores = ['lightgreen','yellow','#FFA500','red','sienna']
    desface=(0.1,0,0,0,0)
    plt.pie(cant, labels=calif, colors=colores,autopct='%1.2f%%', explode=desface)
    plt.title('Area de Logistica y Servicios Chalet')

    data={

            "ALSCcantMB":ALSCcantMB,
            "ALSCcantB":ALSCcantB,
            "ALSCcantR": ALSCcantR,
            "ALSCcantM": ALSCcantM,
            "ALSCcantMM": ALSCcantMM,
            "porcMB": porcMB,
            "porcB": porcB,
            "porcR": porcR,
            "porcM": porcM,
            "porcMM": porcMM,
            "show": plt.savefig('encuesta/static/encuesta/GALSC.png'),
            "del": plt.close()
            }

    return render(request, 'chalet.html', data)

def ResumenUO(request):
    encuestasUO=Encuesta.objects.filter(area__exact='UO')
    ###Unidad operativa###
    UOcantMB=0
    UOcantB=0
    UOcantR=0
    UOcantM=0
    UOcantMM=0

##Unidad operativa
    for i in encuestasUO:
        if i.servicio_limpieza=='MB':
            UOcantMB+=1
        elif i.servicio_limpieza=='B':
            UOcantB+=1
        elif i.servicio_limpieza=='R':
            UOcantR+=1
        elif i.servicio_limpieza=='M':
            UOcantM+=1
        elif i.servicio_limpieza=='MM':
            UOcantMM+=1

####Metodo para calcular porciento
    total=encuestasUO.count()
    #porciento MB
    porcMB=(UOcantMB*100)/total

    #porciento B
    porcB=(UOcantB*100)/total

    #porciento R
    porcR=(UOcantR*100)/total

    #porciento M
    porcM=(UOcantM*100)/total

    #porciento MM
    porcMM=(UOcantMM*100)/total

    data={

            "UOcantMB":UOcantMB,
            "UOcantB":UOcantB,
            "UOcantR": UOcantR,
            "UOcantM": UOcantM,
            "UOcantMM": UOcantMM,
            "porcMB": porcMB,
            "porcB": porcB,
            "porcR": porcR,
            "porcM": porcM,
            "porcMM": porcMM,
            }

    return render(request, 'unidad_operativa.html', data)

def Resumen(request):
    return render(request, 'menu_resumen.html')

