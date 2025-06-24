from django import forms
from .models import *


class MobileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MobileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mobile
        fields = "__all__"
        exclude = ('user', )