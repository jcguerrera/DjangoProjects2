from django.shortcuts import render, HttpResponse
import requests


# Create your views here.
def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value}
            response = requests.post('http://127.0.0.1:8000/hygrometer/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/hygrometer/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})

def participante(request):
    print ('entre a participante')
    if 'cedula' in request.GET:
        print('entre al if')
        cedula = request.GET['cedula']
        nombre = request.GET['nombre']
        actividad = request.GET['actividad']
        estrato = request.GET['estrato']
        #valor = request.GET['value']
        print(request.GET)

       # Verifica si el value no esta vacio
        if cedula:
        # Crea el json para realizar la petición POST al Web Service
            args = {'cedula': cedula, 'nombre': nombre, 'actividad': actividad, 'estrato': estrato}
            print(args)
            response = requests.post('https://pi1-eafit-jcguerrera-cagarciap.azurewebsites.net/participante/', args)
            # Convierte la respuesta en JSON
            medicion_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('https://pi1-eafit-jcguerrera-cagarciap.azurewebsites.net/participante/')
    # Convierte la respuesta en JSON
    datos = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/participantes.html", {'datos': datos})