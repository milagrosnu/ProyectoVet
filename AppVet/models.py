from django.db import models

# Create your models here.
#Alumno
class Services(models.Model):
    service_name = models.CharField(max_length=50)
    service_prof = models.CharField(max_length=50)
    service_available = models.BooleanField(default=True)

    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service_name} a cargo de {self.service_prof}'

#Profesor
class Booking(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_owner = models.CharField(max_length=50)
    owner_mail = models.EmailField()
    booked_service = models.CharField(max_length=50)
    booked_day = models.DateField()
    booked_time = models.TimeField()

    add_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'El dia {self.booked_day} - {self.booked_time} se debe realizar {self.booked_service}'


#Curso
class Product(models.Model):
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=100)
    prod_stock = models.IntegerField()
    prod_img = models.ImageField()
    prod_price = models.IntegerField()

    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-prod_id']
    def __str__(self):
        return f'El {self.prod_name} tiene cantidad de: {self.prod_stock}'
