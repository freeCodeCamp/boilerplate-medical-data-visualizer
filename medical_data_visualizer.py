import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# 2
# Convert height from cm to meters
df['height'] = df['height'] / 100

# Calculate BMI
df['BMI'] = df['weight'] / (df['height'] ** 2)

# Determine overweight status
df['overweight'] = (df['BMI'] > 25).astype(int)
df = df.drop(columns=['BMI'])
# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # Crear DataFrame en formato largo
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable', value_name='value')
    
    # Crear el gráfico categórico
    cat_plot = sns.catplot(data=df_cat, x='value', col='cardio', hue='variable', kind='count', height=4, aspect=1)


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig