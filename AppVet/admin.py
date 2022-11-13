from django.contrib import admin
from .models import Services, Product, Booking

# Register your models here.
admin.site.register(Services)
admin.site.register(Product)
admin.site.register(Booking)