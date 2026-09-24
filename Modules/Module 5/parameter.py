def hello(name):
    print(f"Hello {name}!")
hello("Nick")
hello("sarah")
hello("Nevaeh")

def add_numbers(num1,num2):
    print(num1+num2)

add_numbers(3,4)
add_numbers(3,22)

def dog_info(age,name):
    print(f"Hi! This is my dog {name} and he is {age} years old!")
dog_info(18,"Jaclin")

def double(number):
    return number*2
print(double(8))

def uppercase(text):
    return text.upper()
names = ["jaclin", "nevaeh", 'aaliyah']

for names in names:
    print(uppercase(names))
