from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('<int:number>', views.show_details),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.delete),
    path('add_show', views.add_show),
    path('edit_show', views.edit_show),
]
