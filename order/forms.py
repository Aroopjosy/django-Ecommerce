from django import forms
from .models import Address
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
        street_address = forms.CharField(
                widget=forms.TextInput(attrs={
                        'placeholder':"1234 Main St",'class':"form-control"}))
        apartment_address = forms.CharField(
                required= False, widget=forms.TextInput(
                        attrs={'placeholder':"Apartment or suite", 'class':"form-control" }))
        country = CountryField(
                blank_label= '(slect country)').formfield(
                        widget=CountrySelectWidget( 
                                attrs= {'class':"custom-select d-block w-100" }))
        zip_code  = forms.CharField(
                widget=forms.TextInput(
                        attrs={'class':"form-control" }))   


    

