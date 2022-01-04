from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from ogatech_app.models import UserProfileInfo
# from ogatech_project.ogatech_app.models import ShippingAddress

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('phone_number', 'address1', 'address2', 'zip_code', 'city', 'country')

# class AddressModelOtechForm(forms.ModelForm):
#     class Meta():
#         model = AddressModelOtech
#         fields = ('address1', 'address2', 'zip_code', 'city', 'country')

# class ShippingAddressForm(forms.ModelForm):
#     class Meta():
#         model = ShippingAddress
#         fields = ('address1', 'address2', 'zip_code', 'city', 'country')