import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# 2
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Añadir la columna overweight
df['overweight'] = df.apply(lambda x: 1 if x['weight'] / (x['height'] / 100) ** 2 > 25 else 0, axis=1)

# 4
def draw_cat_plot():
    # Crear DataFrame en formato largo
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                    var_name='variable', value_name='value')

    # Agrupar y contar los valores
    df_cat_counts = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Crear el gráfico categórico
    g = sns.catplot(data=df_cat_counts, x='variable', y='total', col='cardio', hue='value', kind='bar', height=4, aspect=1)

    # Obtener la figura desde el objeto catplot
    fig = g.fig

    # Mostrar el gráfico
    plt.show()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # Limpiar los datos
    df_heat = df[
        (df['ap_hi'] >= df['ap_lo']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular la matriz de correlación
    corr = df_heat.corr()

    # Generar una máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(12, 10))

    # Graficar la matriz de correlación usando sns.heatmap()
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=.5, ax=ax, cbar_kws={"shrink": .5})

    # Mostrar el gráfico
    plt.show()

    # 16
    fig.savefig('heatmap.png')
    return fig