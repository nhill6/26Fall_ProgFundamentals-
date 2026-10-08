def rectangle_stats(length,width): #created function
    area = length * width #area = length times width
    perimeter = (length + width) * 2 #perimeter =Length + width +Length + Width 
    return area , perimeter 
height = int(input("What is the length of your rectangle: ")) #user input
wide = int(input("What is the width of your rectangle: "))

area, perimeter = rectangle_stats(height,wide) # takes the user for length and width and then takes the returned values and stores them in area and perimeter 
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")