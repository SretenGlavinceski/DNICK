from django import forms
from .models import *


class CakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CakeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

        # Set specific placeholders or attributes
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter name',
        })
        self.fields['price'].widget.attrs.update({
            'placeholder': 'Enter price',
        })
        self.fields['weight'].widget.attrs.update({
            'placeholder': 'Enter weight',
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Enter description',
        })

        # Optionally change labels and help texts
        self.fields['image'].label = 'Choose an image'
        # self.fields['price'].help_text = 'Maximum total price should not exceed $10,000'


    class Meta:
        model = Cake
        fields = '__all__'
        exclude = ('baker', )
