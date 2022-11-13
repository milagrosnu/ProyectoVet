from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from .forms import *

# Create your views here.

#Inicio
def index(request):
    return render(request, 'AppVet/index.html')

#Servicios
def ShowServices(request):
    return render(request, 'AppVet/services.html')

#Traer servicios cargados ddbb
""" def GetServices(request):
    return render(request, 'AppVet/services_mgt.html')
 """
""" def GetService(request, id):
    service = None
    service = Services.objects.GET(id=id)
    context = {'service': service}
    return render(request, 'AppVet/services_mgt.html', context)
 """
#Crear servicio
def CreateService(request):
    if request.method == 'POST':
        s_form = ServicesForm(request.POST)
        if s_form.is_valid():
            data = s_form.cleaned_data
            service = Services(
                service_name=data['service_name'],
                service_prof=data['service_prof'],
                service_available=data['service_available'],
            )
            service.save()
            return render(request, 'AppVet/services_mgt.html')
        else:
            redirect('services')
    e_form = ServicesForm()
    return render(request, 'AppVet/services.html', {'form': e_form})

#Armar lista de servicios
def GetServices(request):
    services = Services.objects.all()
    context = {'services' : services}
    return render(request, 'AppVet/services_mgt.html', context)

#Actualizar servicio
def UpdateService(request, id):
    service = Services.objects.GET(id=id)
    form = ServicesForm(instance=service)

    if request.method == 'POST':
        form = ServicesForm(request.POST, instance = service)

        if form.isvalid():
            form.save()
            return redirect('GetServices')
    
    context = {'form': form}
    return render(request, 'services.html', context)

def DeleteService(request, id):
    service = Services.objects.get(id=id)

    if request.method == 'POST':
        service.delete()
        return redirect('GetServices')
    context = {'object': service}
    return render(request, 'AppVet/services-mgt.html', context)

#Productos
def ShowProducts(request):
    return render(request, 'AppVet/products.html')

#Reservas
def ShowBookings(request):
    return render(request, 'AppVet/bookings.html')