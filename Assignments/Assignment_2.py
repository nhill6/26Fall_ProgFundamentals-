import time
from hs3003 import HS3003

sensor = HS3003()

while True:
    t, h = sensor.read()
    print(f"Temp: {t:.1f} C Humidity: {h:.1f}%") #f string to print emp and humidity 
    time.sleep(2)
    t1, h = sensor.read()
    print(f"Temp: {t1:.1f} C Humidity: {h:.1f}%")
    time.sleep(2)
    t2, h = sensor.read()
    print(f"Temp: {t2:.1f} C Humidity: {h:.1f}%")
    time.sleep(2)
    t3, h = sensor.read()
    print(f"Temp: {t3:.1f} C Humidity: {h:.1f}%")
    time.sleep(2)
    t4, h = sensor.read()
    print(f"Temp: {t4:.1f} C Humidity: {h:.1f}%")
    time.sleep(2)
 
    if t >= 32 and t <= 48:
        print("The temperature is high!")


    elif t >= 23 and t <= 31: #this is the range for normal temperature 
        print("The temperature is normal!")
        

    elif t >= 10 and t <= 22:
        print("The temperature is low!") #This is the print stantement for a low terperature

    tempAverage = (t+t1+t2+t3+t4)/5 #adds up the first five termpetures than divides them by 5 to find average 
    print (f"The Temperature Average is: {tempAverage}")

   
