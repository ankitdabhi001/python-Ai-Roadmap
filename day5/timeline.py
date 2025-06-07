# Print a countdown

import time

a=int(input("enter your time in second : "))

for i in range(a,0,-1):
    print(f"time is :{i}")

    time.sleep(1)

print("your time is up...!")

