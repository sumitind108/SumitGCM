from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plot/', views.process_and_plot, name='process_and_plot'),
]
