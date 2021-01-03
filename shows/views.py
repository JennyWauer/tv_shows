from django.shortcuts import render, redirect

from .models import *

def index(request):
    context = {
        "shows": Show.objects.all(),
        "networks": Network.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    context = {
        "networks": Network.objects.all()
    }
    return render(request, 'new.html', context)

def show_details(request, number):
    context = {
        "show": Show.objects.get(id=number)
    }
    return render(request, 'show-details.html', context)

def edit(request, number):
    context = {
        "networks": Network.objects.all(),
        "show_edit": Show.objects.get(id=number)
    }
    return render(request, 'edit.html', context)

def delete(request, number):
    show_to_delete = Show.objects.get(id=number)
    show_to_delete.delete()
    return redirect('/shows')

def add_show(request):
    if request.method == 'GET':
        return redirect('/shows')
    if request.method == 'POST':
        Show.objects.create(title=request.POST['title'],network=Network.objects.get(name=request.POST['network']),release_date=request.POST['release_date'],desc=request.POST['desc'])
        return redirect('/shows')

def edit_show(request):
    if request.method == 'GET':
        return redirect('/shows')
    if request.method == 'POST':
        show_to_edit = Show.objects.get(id=request.POST['show_id'])
        show_to_edit.title = request.POST['title']
        show_to_edit.network = Network.objects.get(name=request.POST['network'])
        show_to_edit.release_date = request.POST['release_date']
        show_to_edit.desc = request.POST['desc']
        show_to_edit.save()
        return redirect('/shows')