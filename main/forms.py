from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['date', 'status', 'type', 'category', 'subcategory','sum','comment']
        widgets = {
                    'date': forms.DateInput(attrs={'type': 'date'})}