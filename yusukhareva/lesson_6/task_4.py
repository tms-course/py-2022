#ДОДЕЛАТЬ
"""
"""
import pandas as pd


df = pd.read_json (r'task3.json', orient='columns')
df.to_csv(r'task4.csv', index = None , sep=',', header = r'task3.json')
task4 = pd.read_csv('task4.csv')
task4.writeheader ['task3.json', 'phone']
print (df)