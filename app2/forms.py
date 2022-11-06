from dataclasses import fields
from django import forms
from . import models

u_type = [("Admin","Admin"),("Buyer","Buyer"),("Seller", "Seller")]

class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Logins
        fields = '__all__'

# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = models.ContactUs
#         fields = '__all__'

class RegistrationForm(forms.ModelForm):
    usertype = forms.CharField(widget=forms.Select(choices=u_type))
    class Meta:
        model = models.Registration
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = '__all__'


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'