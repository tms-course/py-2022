import time 
from datetime import datetime 
datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')

n = int(input("Enter the number: "))
date_time_list = [i for i in range (n)]
lst=[]
for i in date_time_list:
    
    time.sleep(1)
    lst.append(datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'))
    i+=1

print (lst)
    
