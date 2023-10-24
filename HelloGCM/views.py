from django.shortcuts import render
from .plotter import process_and_plot_csv

# Create your views here.

def index(request):
    return render(request, 'HelloGCM/index.html')



def plot_graph(request):
    # Call the function from plotter.py to process CSV and plot graph
    plot_path = process_and_plot_csv()

    # Print the plot path for debugging
    print("Plot Path:", plot_path)

    # Render the template with the plot
    return render(request, 'HelloGCM/plot_template.html', {'plot_path': plot_path})