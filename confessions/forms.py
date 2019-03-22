from django import forms
from confessions.models import ConfessionTable

class ConfessionForm(forms.ModelForm):
    class Meta:
        model=ConfessionTable
        fields=('text',)
    
    
#widget=forms.Textarea