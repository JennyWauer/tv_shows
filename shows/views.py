from django.shortcuts import render, redirect

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
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],desc=request.POST['desc'])
            return redirect('/shows')

def edit_show(request):
    if request.method == 'GET':
        return redirect('/shows')
    if request.method == 'POST':
        number = int(request.POST['show_id'])
        show_to_edit = Show.objects.get(id=request.POST['show_id'])
        edit_errors = Show.objects.basic_validator(request.POST)
        if len(edit_errors) > 0:
            for key, value in edit_errors.items():
                messages.error(request, value)
            return redirect('/shows/<int:number>/edit')
        else:
            show_to_edit.title = request.POST['title']
            show_to_edit.network = request.POST['network']
            show_to_edit.release_date = request.POST['release_date']
            show_to_edit.desc = request.POST['desc']
            show_to_edit.save()
            return redirect('/shows')