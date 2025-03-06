"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""

#import counter library
from corner import corner
#importing matplotlib for visualization of graphs
import matplotlib.pyplot as plt
#import numpy for numerical operations
import numpy as np
#import pandas for data mainipulation
import pandas as pd
#this library used for statistical calculations like skewness and kurtosis
import scipy.stats as ss
#Seaborn for data visualization
import seaborn as sns


def plot_relational_plot(df):
    """Histogram Plot for Opening Stock Prices."""
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Open'], bins=50, kde=True)
    plt.title("Histogram Of Opening Price")
    plt.xlabel("Open Price")
    plt.ylabel("Frequency")
    plt.grid()
    plt.savefig('relational_plot.png')
    plt.show()

def plot_categorical_plot(df):
    """Plots a Pie chart to show average stock price for Open, High, Low and Close"""
    plt.figure(figsize=(8, 8))
    mean_values = df[['Open', 'High', 'Low', 'Close']].mean()
    plt.pie(mean_values, labels=mean_values.index, autopct='%1.1f%%', startangle=140)
    plt.title("Average Stock Price Distribution Of Opening Price")
    plt.savefig('categorical_plot.png')
    plt.show()


def plot_statistical_plot(df):
    """Violin Plot to show Opening Stock Price"""
    plt.figure(figsize=(10, 5))
    sns.violinplot(y=df['Open'])
    plt.title("Violin Plot of Open Prices")
    plt.ylabel("Open Price")
    plt.savefig('statistical_plot.png')
    plt.show()


def statistical_analysis(df, col: str):
    """Calculates and returns statistical moments (mean, stddev, skewness, kurtosis) for a given column."""
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col])
    excess_kurtosis = ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    """Preprocessing The data, showing null values, top 5 rows, summary, information etc."""
    print("\nTop 5 Rows:")
    print(df.head())
    print("\nInformation Of Dataset:")
    print(df.info())
    print("\nNull Values:")
    print(df.isnull().sum())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nCorrelation Matrix:")
    print(df.corr())
    return df


def writing(moments, col):
    """Prints a summary of statistical moments and data distribution characteristics"""
    output = (f'\nFor the attribute {col}:'
              f'\nMean = {moments[0]:.2f}, '
              f'Standard Deviation = {moments[1]:.2f}, '
              f'Skewness = {moments[2]:.2f}, and '
              f'Excess Kurtosis = {moments[3]:.2f}.')
    
    skew_text = "not skewed" if abs(moments[2]) < 2 else ("right-skewed" if moments[2] > 0 else "left-skewed")
    kurtosis_text = "mesokurtic" if abs(moments[3]) < 2 else ("leptokurtic" if moments[3] > 0 else "platykurtic")
    
    output += f'\nThe data was {skew_text} and {kurtosis_text}.'
    print(output)


def main():
    df = pd.read_csv(r'C:\Users\prapu\Desktop\Prapul-20250306T101609Z-001\Prapul\data.csv', parse_dates=['Date'], index_col='Date')
    df = preprocessing(df)
    col = 'Open'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()

