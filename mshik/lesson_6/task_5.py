"""
Задание 5*.

Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме возраста.
"""
import pandas as pd
from os.path import dirname, abspath


DATA_DIR = f"{abspath(dirname(__file__))}/data/"


# Remove age from users dataframe
users_df = pd.read_csv(DATA_DIR + "users.csv")
users_df.drop("age", inplace=True, axis=1)

# Write users dataframe without age to excel file
users_df.to_excel(DATA_DIR + "users.xlsx")