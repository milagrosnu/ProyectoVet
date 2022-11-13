from django.forms import ModelForm
from .models import Booking, Product, Services

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'