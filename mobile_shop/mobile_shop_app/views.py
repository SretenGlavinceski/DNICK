from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    mobiles = Mobile.objects.all()
    return render(request, 'index.html', {'mobiles': mobiles, 'title': 'All Phones'})


def view_details(request, id_mobile):
    mobile = Mobile.objects.filter(id=id_mobile).first()
    return render(request, 'view-details.html', {'mobile': mobile, 'title': 'Phone Details'})


def create(request):
    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            mobile = form.save(commit=False)
            mobile.user = request.user
            mobile.save()

        return redirect('index')

    form = MobileForm()
    return render(request, 'add-mobile.html', {'form': form, 'title': 'Add New Phone'})
