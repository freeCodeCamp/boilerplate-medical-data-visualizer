import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
for ind, row in df.iterrows():
    df.loc[ind, "overweight"]=(row['weight'])/((row['height']/100)**2)

for ind, row in df.iterrows():
    if ((row['weight'])/((row['height']/100)**2)>25):
        df.loc[ind, "overweight"] = 1
    else:
        df.loc[ind, "overweight"] = 0

df['overweight'] = df.overweight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
for ind, row in df.iterrows():
    if (row['cholesterol'] <= 1):
         df.loc[ind, "cholesterol"] = 0
    else:
        df.loc[ind, "cholesterol"] = 1

for ind, row in df.iterrows():
    if (row['gluc'] <= 1):
         df.loc[ind, "gluc"] = 0
    else:
        df.loc[ind, "gluc"] = 1

ht_df =df

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['id', 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], value_vars= ['cardio'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    g = df_cat.groupby(['value'])

    t_v = g.get_group(0)
    t_v.count() # cardio, value =0 
    t_v1 = g.get_group(1)
    t_v1.count() # cardio, value =1

    df_catm = df_cat[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke','value']]
    df_catm = df_cat.melt(id_vars='value', var_name = 'variable', value_name = 'Total')
    df_cat = df_catm.rename(columns={'value':'cardio'})
    

    
    # Draw the catplot with 'sns.catplot()'
    
    ax = sns.catplot(x= 'variable', y = 'Total', data = df_cat, estimator = len, kind = 'bar',hue = 'Total', col='cardio', legend = False)
    plt.legend(title= 'value', bbox_to_anchor=(1.15, .55))
    plt.show(ax)


    # Get the figure for the output
    fig = ax


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = ht_df
    df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025)) & (df_heat['height']<= df_heat['height'].quantile(0.975))]
    df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & (df_heat['height']<= df_heat['height'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr().round(2)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10,10))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, annot = True, Vmax =1, vmin= 0, mask = mask, ax= ax)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
