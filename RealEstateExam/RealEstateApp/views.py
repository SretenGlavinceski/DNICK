from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    properties = Property.objects.filter(is_sold=False, area__gt=100).all()
    return render(request, 'index.html', {'properties': properties, 'title': 'All Properties'})


def edit_property(request, id_property):
    property = Property.objects.filter(id=id_property).first()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()

            # delete all old characteristics about the property

            PropertyCharacteristics.objects.filter(property_id=property.id).delete()

            # Add the new characteristics

            new_char_names = request.POST.get('chars').split(',')
            for characteristic_name in new_char_names:
                char = Characteristic.objects.filter(name=characteristic_name).first()
                PropertyCharacteristics.objects.create(characteristic=char, property=property)

        return redirect('index')

    form = PropertyForm(instance=property)
    return render(request, 'edit-property.html', {'form': form, 'title': 'Edit Property'})
