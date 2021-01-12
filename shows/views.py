from django.shortcuts import render, redirect, reverse

from .models import *

from django.contrib import messages

def index(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def show_details(request, number):
    context = {
        "show": Show.objects.get(id=number)
    }
    return render(request, 'show-details.html', context)

def edit(request, number):
    context = {
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
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],desc=request.POST['desc'])
        return redirect('/shows')

def edit_show(request):
    if request.method == 'GET':
        return redirect('/shows')
    if request.method == 'POST':
        show_to_edit.title = request.POST['title']
        show_to_edit.network = request.POST['network']
        show_to_edit.release_date = request.POST['release_date']
        show_to_edit.desc = request.POST['desc']
        show_to_edit.save()
        return redirect('/shows')