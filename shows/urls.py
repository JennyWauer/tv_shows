from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('<number>', views.show_details),
    path('<number>/edit', views.edit),
    path('<number>/delete', views.delete),
    path('add_show', views.add_show),
]
