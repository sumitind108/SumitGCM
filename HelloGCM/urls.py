from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='index'),
    path('plot/', views.process_and_plot, name='process_and_plot'),

    path('plot_template/', views.plot_template, name='plot_template'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
