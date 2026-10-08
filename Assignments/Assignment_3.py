import time
from hs3003 import HS3003

sensor = HS3003()
def tempread(): #created a function using sensor read but only displays the temperature
    t,h = sensor.read()
    print(f"Temp: {t:.1f} C")
    time.sleep(2)
def humidread(): #created a function using sensor read but only displays the humidity
    t, h = sensor.read()
    print(f"Humidity: {h:.1f}%") 
    time.sleep(2)

while True:
    choice = input("Choose one : T - temperature, H - Humidity, 0 - Both: ") #gives the user 3 options to choose from 
    if choice == "T": #if T is chosen temperture will be displayed
        tempread()
        break #this break allows the code to continue even if T isn't chosen
    elif choice == "H": #if H is chosen humidity will be displayed
        humidread()
        break #this break allows the code to continue even if H isn't chosen
    elif choice == "0": #if 0 is chosen both will be displayed
        t, h = sensor.read()
        print(f"Temp: {t:.1f} C Humidity: {h:.1f}%") #f string to print emp and humidity 
        time.sleep(2)
        break #this break allows the code to continue even if none of the options are chosen
    else:
        print("Error, please choose one of the options") # if non of the options are chosen code won't run and the user will be told to pick one of the following options
