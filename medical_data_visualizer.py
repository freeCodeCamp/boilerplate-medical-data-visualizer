import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = None
df = pd.read_csv('./medical_examination.csv')

# Add 'overweight' column
df['bmi']=((df.weight)/((df.height/100)**2)).round(0) # se agrega el campo y se calcula el valor de bmi

# se agrega el campo y se calcula el valor sobrepeso

# https://www.delftstack.com/es/howto/python-pandas/pandas-apply-multiple-columns/
def calc_overw(a): #def calc_overw(a):
    if a[13] > 25: # a
        return round(1,0)
    else:
        return round(0,0)

# otro metodo en python
# df['overweight'] = [0 if x/((y/100)**2)<=25 else 1 for x,y in zip(df['weight'], df['height'])]

df['overweight'] = df.apply(calc_overw, axis = 1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def norm_chol(a):
    if a[7] == 1:
        return round (0, 0)
    if a[7] >= 2: # a
        return round (1, 0)

def norm_gluc(a):
    if a[8] == 1:
        return round (0, 0)
    if a[8] >= 2: # a
        return round (1, 0)

# otro metodo
# df['cholesterol'] = [0 if x==1 else 1 for x in df['cholesterol']]
# df['gluc'] = [0 if x==1 else 1 for x in df['gluc']]

df['cholesterol'] = df.apply(norm_chol, axis = 1)
df['gluc'] = df.apply(norm_gluc, axis = 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # df_cat = None
    # df_cat = pd.DataFrame({'cardio':df.cardio, 'active':df.active, 'alco':df.alco, 'cholesterol':df.cholesterol, 'gluc':df.gluc, 'overweight':df.overweight, 'smoke':df.smoke})
    # df_cat = pd.melt(df_cat, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'], value_name='value')
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'],value_name='value')
    
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.size.html?highlight=size#pandas.core.groupby.GroupBy.size
    df_cat_grouped = df_cat.groupby(['cardio','variable', 'value'], as_index = False).size().rename(columns={'size':'total'})

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat_grouped, kind='bar', ci=None)

    # Do not modify the next two lines
    fig = g.fig
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # df.head()
    # df.age.count() # 70000

    # Clean the data
    # df_heat = None
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html?highlight=quantile#pandas.DataFrame.quantile
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
             (df['height'] >= df['height'].quantile(0.025)) & 
             (df['height'] <= df['height'].quantile(0.975)) & 
             (df['weight'] >= df['weight'].quantile(0.025)) &
             (df['weight'] <= df['weight'].quantile(0.975))]
    
    # df_heat.age.count() # 63259

    # Calculate the correlation matrix
    # corr = None
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html?highlight=corr#pandas.DataFrame.corr
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    # mask = None
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html?highlight=corr#pandas.DataFrame.corr
    # https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    # fig, ax = None
    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    # https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap
    ax = sns.heatmap(corr, annot=True, fmt=".1f", square=True, mask=mask, center=0)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
