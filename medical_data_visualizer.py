import pandas as pd

# 1 - Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# 2 - Create the overweight column in the df variable
df['overweight'] = None

# 3 - Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)


# 4 - Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot(
    data = df, x = 'cholesterol', y = 'gluc', hue = 'smoke', col = 'cardio', kind = 'bar'
):
      
    # 5 - Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = 


    # 6 - Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to
    df_cat = None
    

    # 7 - Draw the catplot with 'sns.catplot()'



    # 8 - Get the figure for the output
    fig = None


    # 9 - Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# 10 - Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 11 - Clean the data
    df_heat = None

    # 12 - Calculate the correlation matrix
    corr = None

    # 13 - Generate a mask for the upper triangle
    mask = None



    # 14 - Set up the matplotlib figure
    fig, ax = None

    # 15 - Draw the heatmap with 'sns.heatmap()'



    # 16 - Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
