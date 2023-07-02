from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
import datetime, os

class Person(object):
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

# Se le denomina como una vista
# Session No.2
def saludo(request):
    # Abrimos el documento externo
    externalDoc = open(os.getcwd().replace("\\", "/") + "/myproject/views/greeting.html")
    # Creamos una plantilla HTML a partir de ese documento
    template = Template(externalDoc.read())
    # Cerramos el documento
    externalDoc.close()
    # Creamos el contexto.Argumento que se paasa al render.
    context = Context()
    # Armamos el documento.
    document = template.render(context)

    return HttpResponse(document)

def get_date(req):
    currentDate = datetime.datetime.now()
    doc = """
    <html>
    <body>
    <h1>This is the current date and time: %s</h1>
    </body>
    </html>""" % currentDate

    return HttpResponse(doc)

# Session No.3
def get_name(request):
    #name = "Luis Daniel"
    #lastName = "García Leal"
    newPerson = Person("Luis Daniel", "García Leal")
    # Abrimos el documento externo
    externalDoc = open(os.getcwd().replace("\\", "/") + "/myproject/views/showname.html")
    # Creamos una plantilla HTML a partir de ese documento
    template = Template(externalDoc.read())
    # Cerramos el documento
    externalDoc.close()
    # Creamos el contexto.Argumento que se pasa al render.
    context = Context({"person_name": newPerson.name , "last_name": newPerson.lastName})
    # Armamos el documento.
    document = template.render(context)

    return HttpResponse(document)

# Session No.4
def get_data(request):
    #name = "Luis Daniel"
    #lastName = "García Leal"
    newPerson = Person("Luis Daniel", "García Leal")
    # Abrimos el documento externo
    externalDoc = open(os.getcwd().replace("\\", "/") + "/myproject/views/session4.html")
    # Creamos una plantilla HTML a partir de ese documento
    template = Template(externalDoc.read())
    # Cerramos el documento
    externalDoc.close()
    # Creamos el contexto.Argumento que se pasa al render.
    context = Context({"person_name": newPerson.name , "last_name": newPerson.lastName, "subjects":["Plantillas", "Modelos", "Formularios", "Vistas", "Despligues"]})
    # Armamos el documento.
    document = template.render(context)
    return HttpResponse(document)

# Session No.5
def session_5(request):
    newPerson = Person("Luis Daniel", "García Leal")
    # Utilizamos el Loader para simplificar el codigo realizado
    template = loader.get_template("session5.html")
    # Renderizamos con un diccionario directamente.
    document = template.render({"person_name": newPerson.name , "last_name": newPerson.lastName, "subjects":["Plantillas", "Modelos", "Formularios", "Vistas", "Despligues"]})
    return HttpResponse(document)

# Session No.6
def session_6(request):
    # En esta sesion se simplificara el codigo inicial.
    newPerson = Person("Luis Daniel", "García Leal")
    return render(request, "session6.html", {"person_name": newPerson.name , "last_name": newPerson.lastName, "subjects":["Plantillas", "Modelos", "Formularios", "Vistas", "Despligues"]})


# Session No.7 
def session_7(request):
    return render(request, "session7.html")