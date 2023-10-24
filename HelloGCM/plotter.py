import matplotlib
matplotlib.use('Agg')  # Use Agg backend

import pandas as pd
import matplotlib.pyplot as plt
from django.conf import settings
import os

def process_and_plot_csv():
    # Get the path to the CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'data', 'can_data.csv')
    print(f"CSV File Path: {csv_file_path}")

    # Read data from CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Your data processing and plotting logic here
    # For example, assuming your CSV file has 'Timestamp', 'Engine_RPM', and 'Vehicle_Speed' columns
    plt.figure(figsize=(10, 6))
    plt.plot(df['Timestamp'], df['Engine_RPM'], marker='o', label='Engine RPM')
    plt.plot(df['Timestamp'], df['Vehicle_Speed'], marker='o', label='Vehicle Speed')
    # Add other columns similarly

    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.title('CAN Data')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image file
    plot_path = os.path.join(settings.STATIC_ROOT, 'plot.png')
    plt.savefig(plot_path)

    return plot_path  # Return the path to the saved plot
