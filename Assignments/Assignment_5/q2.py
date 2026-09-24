def rectangle_stats(length,width):
    area = length * width
    perimeter = (length + width) * 2
    return area , perimeter
height = int(input("What is the lenght: "))
wide = int(input("What is the width: "))

area, perimeter = rectangle_stats(height,wide)
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")