from django import forms
from .models import *


class PropertyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

        self.fields['area'].label = 'Area (in sq. meters)'
        self.fields['date_released'].label = 'Date Announced for Sale'
        self.fields['image'].label = 'Photo'
        self.fields['is_reserved'].label = 'Is this a reserve?'
        self.fields['is_sold'].label = 'Has this location been sold?'

    class Meta:
        model = Property
        fields = '__all__'
