from django import forms
from .models import Record,Type,Category,Subcategory
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["name"]
        widgets = {
            "name" : forms.TextInput(attrs={'placeholder':'Введите тип'})
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name",'type']
        widgets = {
            "name" : forms.TextInput(attrs={'placeholder':'Введите категорию'}),
            'type' : forms.Select()
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name','category']
        widgets = {
            "name" : forms.TextInput(attrs={'placeholder':'Введите подкатегорию'}),
            'category' : forms.Select()
        }
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['date', 'status','type','category','subcategory','sum','comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'sum': forms.NumberInput(attrs={'placeholder': '0.00'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Введите комментарий'}),
        }