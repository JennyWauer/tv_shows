from django.shortcuts import render, redirect

from .models import *

def index(request):
    context = {
        "shows": Show.objects.all(),
        "networks": Network.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def show_details(request, number):
    return render(request, 'show-details.html')

def edit(request, number):
    return render(request, 'edit.html')

def delete(request, number):
    return redirect('/shows')

def add_show(request):
    if request.method == 'GET':
        return redirect('/shows')
    if request.method == 'POST':
        Show.objects.create(title=request.POST['title'],network=Network.objects.get(name=request.POST['network']),release_date=request.POST['release_date'],desc=request.POST['release_date'])
        return redirect('/shows')