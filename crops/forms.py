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
             'description': forms.TextInput(attrs={'class': 'form-control'}),
             'temperature': forms.TextInput(attrs={'class': 'form-control'}),
             'moisture': forms.TextInput(attrs={'class': 'form-control'}),
             #'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        moisture = cleaned_data.get('moisture')
        temperature = cleaned_data.get('temperature')

        if moisture is not None and temperature is not None:
            crop_health = CropHealth(moisture, temperature)
            health_status = crop_health.analyse_health()
            if "Health Risk" in health_status:
                raise forms.ValidationError(health_status)

        return cleaned_data

class DiagnosticsForm(forms.ModelForm):
    class Meta:
        model = Diagnostics
        fields = ['crop_name','appearance', 'leaf_age']
        widgets = {
            'crop_type': forms.TextInput(attrs={'class': 'form-control'}),
            'appearance': forms.Select(attrs={'class': 'form-control'}),
            'leaf_age': forms.Select(attrs={'class': 'form-control'}),
        }