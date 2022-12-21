"""
Прочитать с файломох преобразований выводить на экран).ранённый csv-файл, первой файл и с файломох преобразований выводить на экран).ранить данные
в excel файл кроме воз example.txtрас файломта – имя(str), возраст(int). с файломтолбец и добавив новый столбец “телефон”. с файлом этими данными - ,
не нужен.
"""
import pandas as pd
import openpyxl

df = pd.read_csv('task_4.csv')
droped_df = df.drop(columns=['Age'], axis=1)
df_adding_columns = droped_df.set_axis((['Person {}'.format(i) for i in range(1, len(droped_df) + 1)])).transpose()
print(df_adding_columns)
df_adding_columns.to_excel('task_5.xlsx')
