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
            return render(request, 'AppVet/services_create.html')
        else:
            redirect('services')
    e_form = ServicesForm()
    return render(request, 'AppVet/services_create.html', {'form': e_form})

#Armar lista de servicios
def GetServices(request):
    services = Services.objects.all()
    context = {'services' : services}
    return render(request, 'AppVet/services_show.html', context)

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

#Borrar
def DeleteService(request, id):
    service = Services.objects.get(id=id)
    service.delete()

    services = Services.objects.all()
    context = {'services' : services}
    return render(request, 'AppVet/services_show.html', context)

#Productos
def ShowProducts(request):
    return render(request, 'AppVet/products.html')

def CreateProduct(request):
    if request.method == 'POST':
        p_form = ServicesForm(request.POST)
        if p_form.is_valid():
            data = p_form.cleaned_data
            product = Product(
                prod_name = data['prod_name'],
                prod_stock = data['prod_stock'],
                prod_img = data['prod_img'],
                prod_price = data['prod_price'],
            )
            product.save()
            return render(request, 'AppVet/products.html')
        else:
            redirect('products')
    e_form = ProductForm()
    return render(request, 'AppVet/products.html', {'form': e_form})

#Armar lista de productos
def GetProducts(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'AppVet/products.html', context)

#Reservas
def ShowBookings(request):
    return render(request, 'AppVet/bookings.html')