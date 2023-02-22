"""
Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме столбца с возрастом.
"""
import pandas as pd

df = pd.read_csv('data.csv')
# remove age column
df.drop('age', axis=1, inplace=True)

# change index names by set-axis() method and use transpose() method
df_transpose = df.set_axis(['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5', 'Person 6']).transpose()

df_transpose.to_excel('data.xlsx')
