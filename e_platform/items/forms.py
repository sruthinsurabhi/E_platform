from django import forms
from .models import item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select', 'style': 'background-color: #BED0FA;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #BED0FA;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'background-color: #BED0FA;'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #BED0FA;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background-color: #BED0FA;'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control col-md-6'})

class EditItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ('name', 'description', 'price', 'image','is_available')
        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #BED0FA;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'background-color: #BED0FA;'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #BED0FA;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background-color: #BED0FA;'}),
           
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control col-md-6'})

