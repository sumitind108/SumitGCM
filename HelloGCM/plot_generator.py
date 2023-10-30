# import pandas as pd
# import matplotlib.pyplot as plt
# import os
# import matplotlib
# matplotlib.use('Agg')

# def generate_plots():
#     df = pd.read_csv(os.path.join('data', 'can_data.csv'))
#     columns = df.columns[2:]
#     plot_paths = []
#     for column in columns:
#         plt.figure(figsize=(8, 6))
#         plt.plot(df['Timestamp'], df[column], marker='o', linestyle='-', color='b')
#         plt.xlabel('Timestamp')
#         plt.ylabel(column)
#         plt.title(f'{column} over Time')
#         plt.xticks(rotation=45)
#         plt.grid(True)
#         plt.tight_layout()

#         os.makedirs(os.path.join('HelloGCM', 'static'), exist_ok=True)
#         plot_path = os.path.join('HelloGCM', 'static', f'{column}_plot.png')
#         plt.savefig(plot_path)
#         plot_paths.append(plot_path)
#         plt.close()

#     return plot_paths


#-------------------------------------------------


# Import necessary libraries and modules
import pandas as pd
import matplotlib.pyplot as plt
import os
from django.templatetags.static import static
import matplotlib
matplotlib.use('Agg')  # Use Agg backend

# Define the function to generate plots and create URLs
def generate_plots():
    # Read data from CSV file
    df = pd.read_csv(os.path.join('data', 'can_data.csv'))

    # Get column names (excluding 'Timestamp' and 'Vehicle_ID')
    columns = df.columns[2:]

    # Create separate plots for each column
    plot_paths = []
    for column in columns:
        plt.figure(figsize=(8, 6))
        plt.plot(df['Timestamp'], df[column], marker='o', linestyle='-', color='b')
        plt.xlabel('Timestamp')
        plt.ylabel(column)
        plt.title(f'{column} over Time')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # Ensure the directory exists before saving the plot
        os.makedirs(os.path.join('HelloGCM', 'static'), exist_ok=True)

        # Save the plot as an image file inside the static directory
        plot_filename = f'{column}_plot.png'
        plot_path = os.path.join('HelloGCM', 'static', plot_filename)
        plt.savefig(plot_path)
        
        # Generate the absolute URL for the image using the static template tag
        plot_url = static('HelloGCM/' + plot_filename)
        plot_paths.append(plot_url)  # Absolute URL for the image

        plt.close()  # Close the plot to release memory

    return plot_paths
