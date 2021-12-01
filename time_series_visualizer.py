import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(28,9))

    sns.lineplot(data = df, x = "date", y = "value", ax = fig.add_subplot(), color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.xticks(range(35,len(df),180))
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index)
    df['year'] = df.index.year
    df['Month'] = df.index.month_name()
    df_bar = df.groupby(['year', 'Month'])['value'].agg('mean').reset_index()
    months=['January','February','March','April','May','June','July','August','September','October','November','December']

    # Draw bar plot
    sns.set_style('ticks')
    # , palette="rocket"
    g = sns.catplot(data=df_bar, x='year', y='value', kind='bar', hue='Month', hue_order=months, ci=None, legend=False, palette='husl')

    fig = plt.gcf()
    ax = g.ax    
    fig.set_size_inches(9, 9, forward=True)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', title="Month")
    plt.setp(ax.get_legend().get_texts(), fontsize='8')
    plt.setp(ax.get_legend().get_title(), fontsize='8')
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']

    # Draw box plots (using Seaborn)

    fig,(ax1, ax2) = plt.subplots(1, 2, figsize = (28, 9))
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1).set(title = "Year-wise Box Plot (Trend)", xlabel = 'Year', ylabel = 'Page Views')
    sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=months).set(title = "Month-wise Box Plot (Seasonality)", xlabel = 'Month', ylabel = 'Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
