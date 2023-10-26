from django.shortcuts import render
from .plot_generator import generate_plots  # Corrected import statement

def index(request):
    return render(request, 'HelloGCM/index.html')

def process_and_plot(request):
    # Call the function to generate plots
    plot_paths = generate_plots()

    # Render the template with the plot paths
    return render(request, 'HelloGCM/plot_template.html', {'plot_paths': plot_paths})
