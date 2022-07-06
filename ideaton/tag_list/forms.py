from django import forms
from .models import category

class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'



