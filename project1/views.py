from contextvars import Context
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
import datetime
def saludo(request):
    nombre= "Javier"
    apellido= "Brizuela"
    fecha_actual= datetime.datetime.now()
    doc_externo= open("G:/apedido/python/Django/project1/project1/plantillas/MiPlantilla.html")
    plt= Template(doc_externo.read())
    doc_externo.close()
    ctx= Context({"nombre_persona":nombre, "apellido_persona":apellido, "ahora":fecha_actual,"temas":["plantillas", "modelos", "formularios", "vistas", "despliegue"]})
    documento= plt.render(ctx)
    return HttpResponse(documento)