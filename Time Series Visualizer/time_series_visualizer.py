import matplotlib.pyplot as plt  # Importing Matplotlib for creating plots and visualizations
import pandas as pd  # Importing pandas to handle data manipulation and analysis
import seaborn as sns  # Importing Seaborn for creating advanced statistical plots
from pandas.plotting import register_matplotlib_converters  # Handles date-related plotting

# Register date converters to enable proper date parsing in plots
register_matplotlib_converters()

# Import data from CSV, parse dates in the 'date' column, and set 'date' as the index for the DataFrame
df = pd.read_csv('Time Series Visualizer/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by removing the top and bottom 2.5% of values, i.e., filter out outliers in 'value' column
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & 
(df['value'] <= df['value'].quantile(0.975))]

# Function to draw the line plot
def draw_line_plot():
    # Create a figure and axes object with a 16x6 inch size
    fig, ax = plt.subplots(figsize=(16, 6))
    
    # Use Seaborn's lineplot function to draw a line plot with 'date' on the x-axis and 'value' on the y-axis
    ax = sns.lineplot(data=df, x='date', y='value')
    
    # Label the x-axis as 'Date'
    plt.xlabel('Date')
    
    # Label the y-axis as 'Page Views'
    plt.ylabel('Page Views')
    
    # Set the title of the plot to 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save the figure as 'line_plot.png' and return the figure object
    fig.savefig('line_plot.png')
    return fig

# Function to draw the bar plot
def draw_bar_plot():
    # Create a copy of the DataFrame and reset the index to have 'date' as a normal column
    df_bar = df.copy().reset_index()
    
    # Extract the year from the 'date' column and create a new column 'year'
    df_bar['year'] = [d.year for d in df_bar.date]
    
    # Extract the month from the 'date' column and create a new column 'month' as full month names
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]

    # Group by 'year' and 'month' to calculate the average page views for each month in each year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    
    # Unstack the DataFrame to reshape the data so that each month becomes a separate column
    df_bar = df_bar.unstack()

    # Explicitly set the column names to the month names in correct order
    df_bar.columns = ['January','February','March','April','May','June','July','August','September','October','November','December']

    # Draw the bar plot with the modified data, setting the figure size to 15x10 inches
    fig = df_bar.plot(kind='bar', figsize=(15,10)).figure

    # Set an empty title for the plot
    plt.title('')
    
    # Label the x-axis as 'Years'
    plt.xlabel('Years')
    
    # Label the y-axis as 'Average Page Views'
    plt.ylabel('Average Page Views')
    
    # Add a legend to the plot with the title 'Months' and set font size of 15
    plt.legend(title='Months', fontsize=15)

    # Save the figure as 'bar_plot.png' and return the figure object
    fig.savefig('bar_plot.png')
    return fig

# Function to draw the box plot
def draw_box_plot():
    # Create a copy of the DataFrame and reset the index to make 'date' a normal column
    df_box = df.copy().reset_index()
    
    # Extract the year from the 'date' column and create a new column 'year'
    df_box['year'] = [d.year for d in df_box.date]
    
    # Extract the month from the 'date' column and create a new column 'month' as abbreviated month names
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Create a figure with two subplots (ax1 and ax2) in one row and two columns, with a figure size of 40x20 inches
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(40, 20))
    
    # Draw a year-wise box plot on ax1 to show the distribution of page views per year
    sns.boxplot(ax=ax1, x="year", y="value", data=df_box)
    
    # Set the title of ax1 to 'Year-wise Box Plot (Trend)'
    ax1.set_title("Year-wise Box Plot (Trend)")
    
    # Label the x-axis of ax1 as 'Year'
    ax1.set_xlabel("Year")
    
    # Label the y-axis of ax1 as 'Page Views'
    ax1.set_ylabel("Page Views")
    
    # Create a list of month abbreviations to ensure correct month order in the plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw a month-wise box plot on ax2 to show the distribution of page views per month
    sns.boxplot(ax=ax2, x="month", y="value", data=df_box, order=month_order)
    
    # Set the title of ax2 to 'Month-wise Box Plot (Seasonality)'
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    
    # Label the x-axis of ax2 as 'Month'
    ax2.set_xlabel("Month")
    
    # Label the y-axis of ax2 as 'Page Views'
    ax2.set_ylabel("Page Views")

    # Save the figure as 'box_plot.png' and return the figure object
    fig.savefig('box_plot.png')
    return fig
