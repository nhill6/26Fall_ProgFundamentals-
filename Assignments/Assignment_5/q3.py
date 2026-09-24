def check_number(number): #created function
    if number % 2 == 0: #checks the reminder of the number to see if it eqauls zero
       return("even") # if it eqauls 0 its even 
    else:
        return("odd") # if it 1 its odd

num = int(input("Enter a whole number: ")) # user input 
result = check_number(num) #checks to see if the number given by user is add or even 
print(f"{num} is an {result} number.") # print statement 