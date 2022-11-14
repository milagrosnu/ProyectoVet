from django.urls import path
from .views import *

urlpatterns = [
    #Inicio
    path('index/', index, name='index'),
    #Servicios - Productos - Turnos
    path('services/', ShowServices, name='services'),
    path('products/', ShowProducts, name='products'),
    path('bookings/', ShowBookings, name='bookings'),
    #Crear 
    path('services/create-service', CreateService, name='CreateService'),
    #Detalle
    path('services/show-services', GetServices, name='GetServices'),

    #path('services/show-services', GetServices, name='GetServices'),
    #path('services/<str:id>', GetService, name='GetService'),
    #path('services/update-service/<str:id>/', GetService, name='GetService'),
    #path('services/delete-service/<str:id>/', DeleteService, name='DeleteService'),
    #path('', GetServices, name ='GetServices'),
    #path('services/', GetServices, name = 'GetServices'),
]