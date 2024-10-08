import pandas as pd  # Importing pandas to handle data manipulation
import seaborn as sns  # Importing seaborn to create statistical plots
import matplotlib.pyplot as plt  # Importing matplotlib for visualizations
import numpy as np  # Importing numpy for numerical operations

# Import data from a CSV file into a pandas DataFrame
df = pd.read_csv("Medical Data Visualizer/medical_examination.csv")

# Add 'overweight' column by calculating BMI
# BMI = weight (kg) / height (m)^2
BMI = df['weight'] / ((df['height'] / 100) ** 2)

# Create 'overweight' column: assign 1 if BMI > 25 (overweight), else 0 (not overweight)
df['overweight'] = (BMI > 25).astype(int)

# Normalize 'cholesterol' and 'gluc' columns: 
# Set value to 0 if it's 1 (good), and to 1 if it's 2 or 3 (bad)
df['cholesterol'] = df['cholesterol'].replace([1, 2, 3], [0, 1, 1])
df['gluc'] = df['gluc'].replace([1, 2, 3], [0, 1, 1])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for categorical plot using pd.melt
    # 'pd.melt' reshapes the DataFrame to a format suitable for seaborn plotting
    # It takes the 'cardio' column as an identifier, and the listed columns as measured variables
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group the data by 'cardio', 'variable', and 'value' to calculate counts
    # 'size()' computes the group sizes, 'reset_index' renames the resulting DataFrame
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))

    # Create a bar plot using seaborn's 'catplot', separating by 'cardio' column
    # 'x' is the variable, 'y' is the total count, 'hue' separates the values for each variable, and 'col' splits by cardio
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # Save the figure to a PNG file
    fig.savefig('catplot.png')
    
    # Return the figure object
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data by applying specific conditions:
    # Keep rows where systolic pressure (ap_hi) is greater than or equal to diastolic pressure (ap_lo)
    # Remove outliers in height and weight by keeping values between the 2.5th and 97.5th percentiles
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix for the cleaned data
    corr = df_heat.corr()

    # Generate a mask for the upper triangle of the correlation matrix (to avoid redundancy)
    mask = np.zeros_like(corr)  # Create a matrix of zeros with the same shape as the correlation matrix
    mask[np.triu_indices_from(mask)] = True  # Mask the upper triangle

    # Set up the matplotlib figure with a 12x12 inch size
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with seaborn's 'heatmap()' function
    # 'linewidths' sets the width of the lines separating cells, 'annot' adds values in the cells
    # 'mask' applies the upper triangle mask, 'square' makes cells square-shaped, and 'vmin' and 'vmax' set value range
    ax = sns.heatmap(corr, linewidths=.5, annot=True, fmt='.1f', mask=mask, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': .45,'format': '%.2f'})

    # Save the figure to a PNG file
    fig.savefig('heatmap.png')
    
    # Return the figure object
    return fig
