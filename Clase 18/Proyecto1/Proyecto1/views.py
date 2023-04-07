from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader 

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - David")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):
        dia = datetime.datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nomb='David'
    ap='BU'
    dia = datetime.datetime.now()
    notas= [1,2,3,4,5]
    diccionario={'nombre':nomb, 'apellido':ap,'fecha':dia,'notas':notas}
    #miHtml = open("C:/Users/Windows/Desktop/Curso-Python-Backend/Clase 18/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    #miHtml.close() #Cerramos el archivo
    #miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    plantilla= loader.get_template('template1.html')
    documento = plantilla.render(diccionario) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)
