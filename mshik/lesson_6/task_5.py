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

transposed_users_df = pd.DataFrame({
        "id": users_df["id"],
        "name": users_df["name"],
        "phone": users_df["phone"]
    }).set_axis([f"Person{num}" for num in range(1, len(users_df) + 1)]).T

# Write users dataframe without age to excel file
transposed_users_df.to_excel(DATA_DIR + "users.xlsx")