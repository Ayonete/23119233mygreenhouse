from .models import Crop, Diagnostics
from django.forms import ModelForm
from django import forms
from .crophealthlib import CropHealth

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
            'planted_on': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'moisture': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

class DiagnosticsForm(ModelForm):
    class Meta:
        model = Diagnostics
        fields = ['crop_name','appearance', 'leaf_age']
        widgets = {
            'crop_type': forms.TextInput(attrs={'class': 'form-control'}),
            'appearance': forms.Select(attrs={'class': 'form-control'}),
            'leaf_age': forms.Select(attrs={'class': 'form-control'}),
        }