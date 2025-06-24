from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'index.html', {'exhibitions': exhibitions, 'title': 'All Exhibitions'})


def add_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = ExhibitionForm()
    return render(request, 'add-exhibition.html', {'form': form, 'pathURL': request.path, 'title': 'Add Exhibition'})


def edit_exhibition(request, id_exhibition):
    exhibition = Exhibition.objects.filter(id=id_exhibition).first()

    if request.method == 'POST':

        print(request.content_type)

        form = ExhibitionForm(request.POST, request.FILES, instance=exhibition)
        if form.is_valid():
            form.save()

            list_artworks_text = request.POST.get('list_artworks_text', '')
            artworks = [artwork for artwork in list_artworks_text.split(', ')]

            # TODO NOT SPECIFIED

        return redirect('index')

    form = ExhibitionForm(instance=exhibition)
    return render(request, 'add-exhibition.html', {'form': form, 'pathURL': request.path, 'title': 'Edit Exhibition'})
