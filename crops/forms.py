from .models import Crop
from django.forms import ModelForm
from django import forms

# declaring the ModelForm
class EditCropForm(ModelForm):
    
    class Meta:
        # the Model from which the form will inherit from
        model = Crop
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes
        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'}),
             'description': forms.TextInput(attrs={'class': 'form-control'}),
             'temperature': forms.TextInput(attrs={'class': 'form-control'}),
             'moisture': forms.TextInput(attrs={'class': 'form-control'}),
             #'image': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class RunDiagnosticsForm(ModelForm):
    
#     class Meta:
#         model = Diagnostics
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#              'description': forms.TextInput(attrs={'class': 'form-control'}),
#              'temperature': forms.TextInput(attrs={'class': 'form-control'}),
#              'moisture': forms.TextInput(attrs={'class': 'form-control'}),
#         }