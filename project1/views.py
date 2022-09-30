from contextvars import Context
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

import datetime
def saludo(request):
    nombre= "Javier"
    apellido= "Brizuela"
    fecha_actual= datetime.datetime.now()
    doc_externo= loader.get_template('MiPlantilla.html')
    documento= doc_externo.render({"nombre_persona":nombre, "apellido_persona":apellido, "ahora":fecha_actual,"temas":["plantillas", "modelos", "formularios", "vistas", "despliegue"]})
    return HttpResponse(documento)