from django.shortcuts import render, redirect

from .models import *

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def show_details(request, number):
    return render(request, 'show-details.html')

def edit(request, number):
    return render(request, 'edit.html')

def delete(request, number):
    return redirect('/shows')