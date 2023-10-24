from django.urls import path
from HelloGCM.views import plot_graph
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('plot/', plot_graph, name='plot_graph'),
]
