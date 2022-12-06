import time 
from datetime import datetime 

def defered_date():
    time.sleep(1)
    return datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
n = int(input("Enter the number: "))
date_list = [defered_date() for _ in range(n)]
print (date_list)
