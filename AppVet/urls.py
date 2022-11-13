from django.urls import path
from .views import *

urlpatterns = [
    #Inicio
    path('index/', index, name='index'),
    #Servicios
    path('services/', ShowServices, name='services'),
    #Crear servicios cargados en bbdd
    path('services/create-services', CreateService, name='CreateService'),
    #Detalle de servicios
    path('services/show-services', GetServices, name='GetService'),
    #path('services/show-services', GetServices, name='GetServices'),
    #path('services/<str:id>', GetService, name='GetService'),
    #path('services/update-service/<str:id>/', GetService, name='GetService'),
    #path('services/delete-service/<str:id>/', DeleteService, name='DeleteService'),
    #path('', GetServices, name ='GetServices'),
    #path('services/', GetServices, name = 'GetServices'),
    #Productos
    path('products/', ShowProducts, name='products'),

    #Turnos
    path('bookings/', ShowBookings, name='bookings')
]