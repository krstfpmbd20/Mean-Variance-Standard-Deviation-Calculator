import pandas as pd  # Import pandas for data manipulation and analysis
import matplotlib.pyplot as plt  # Import matplotlib for creating visualizations
from scipy.stats import linregress  # Import linregress from scipy for linear regression analysis

def draw_plot():
    # Read data from file
    df = pd.read_csv('Sea Level Predictor/epa-sea-level.csv')  # Read the CSV file containing sea level data into a DataFrame

    # Create scatter plot
    x = df['Year']  # Extract the 'Year' column for the x-axis
    y = df['CSIRO Adjusted Sea Level']  # Extract the 'CSIRO Adjusted Sea Level' column for the y-axis
    fig, ax = plt.subplots(figsize=(6,6))  # Create a figure and axes object with a 6x6 inch size
    ax = plt.scatter(x, y)  # Create a scatter plot with the extracted x and y data

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(x, y)  # Perform linear regression on the entire dataset
    x_pred = pd.Series([i for i in range(1880, 2051)])  # Generate x values (years) from 1880 to 2050 for the prediction line
    y_pred = slope * x_pred + intercept  # Calculate the corresponding y values (predicted sea levels) using the slope and intercept from the regression
    plt.plot(x_pred, y_pred, 'r')  # Plot the line of best fit in red ('r') for the entire data range

    # Create second line of best fit
    df_forecast = df.loc[df['Year'] >= 2000]  # Filter the data to include only years from 2000 onwards
    x_forecast = df_forecast['Year']  # Extract the 'Year' column from the filtered dataset
    y_forecast = df_forecast['CSIRO Adjusted Sea Level']  # Extract the 'CSIRO Adjusted Sea Level' column from the filtered dataset

    # Get new slope and intercept for the filtered data (years >= 2000)
    slope, intercept, r_value, p_value, stderr = linregress(x_forecast, y_forecast)  # Perform linear regression on the filtered data
    x_pred2 = pd.Series([i for i in range(2000, 2051)])  # Generate x values (years) from 2000 to 2050 for the second prediction line
    y_pred2 = slope * x_pred2 + intercept  # Calculate the corresponding y values for the second line of best fit
    plt.plot(x_pred2, y_pred2, 'green')  # Plot the second line of best fit in green ('green') for the data from 2000 onwards

    # Add labels and title
    plt.title('Rise in Sea Level')  # Add a title to the plot
    plt.xlabel('Year', fontsize=12)  # Label the x-axis as 'Year' with a font size of 12
    plt.ylabel('Sea Level (inches)', fontsize=12)  # Label the y-axis as 'Sea Level (inches)' with a font size of 12

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')  # Save the plot as a PNG file named 'sea_level_plot.png'
    return plt.gca()  # Return the current axes object for further inspection or testing