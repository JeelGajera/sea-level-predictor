import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15,8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880, 2051)])
    ax.plot(x, res.intercept + res.slope * x, 'r', label='fitted line')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = pd.Series([i for i in range(2000, 2051)])
    ax.plot(x2, res2.intercept + res2.slope * x2, 'g', label='fitted line 2')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # plt.tight_layout()
    # plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
