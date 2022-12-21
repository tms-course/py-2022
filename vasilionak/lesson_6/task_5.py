"""
Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме столбца с возрастом.
"""

import pandas as pd

data = pd.read_csv('file_3.csv')

data.drop('Age', axis=1, inplace= True)

data_transpose = data.set_axis(['Person {i}' for i in range(1, len(data))]).transpose()

data_transpose.to_excel('data.xlsx')
