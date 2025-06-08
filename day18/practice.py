 
# Whether visulizer

import numpy as np
import matplotlib.pyplot as py
tempreture=[]

for a in range(1,8):

    user_input=float(input(f"Enter Day {a} tempreture in celecias : "))
    tempreture.append(user_input)

temp=np.array(tempreture)
days=np.arange(1,8)
mean_data=np.mean(temp)
max_data=np.max(temp)
min_data=np.min(temp)

print("Summirized Temperature is here :\n")

print(f"Average temperature is : {mean_data:.2f}")
print(f"maximum temerature {max_data:.2f}")
print(f"minimum temperature is {min_data:.2f}")

py.title("3 Days Temperature")
py.plot(days,temp,linestyle='-',marker='o',color='red',label="temperature")
py.axhline(mean_data,label="mean temp")
py.xlabel("days")
py.ylabel("tempreture")
py.grid()
py.legend()
py.show()