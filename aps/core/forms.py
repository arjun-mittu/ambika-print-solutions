from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('Paytm', 'Paytm'),
    
)
size_choice=(
    ('XXXL','XXXL'),
    ('XXL','XXL'),
    ('XL','XL'),
    ('L','L'),
    ('M','M'),
    ('S','S'),
    ('XS','XS'),
    ('XXS','XXS')
)
class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'id': 'address',
        'class':'form-control',
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite (optional)',
        'id': 'address-2',
        'class':'form-control',
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'form-control',

        }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'zip'
    }))
    city=forms.CharField(required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
        
    phoneno=forms.IntegerField(required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class contactmefrm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your name',
         'class':'form-control',
    }))
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Your Email',
        'class':'form-control',
    }))
    subject=forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'subject',
         'class':'form-control',
    }))
    message=forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'message',
         'class':'form-control',
         
    }))

