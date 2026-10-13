cafe_name = "***Python Café***"
tax_rate = 0.08
#a function that greets the user
def greet(name):
    print(f"Welcome to Python Café, {name}!")
#Varibles that have menu items stored inside
menu = {"espresso": 3.00, "latte": 4.50, "matcha": 4.25, "mocha": 5.00, "muffin": 2.50, "croissant": 3.25,}
order = []
#a series of functions that use the lists above to put into the parameters to get the output
def show_menu(menu):
    for item, price in menu.items():
       print(f"{item}: {price:.2f}")
def show_order(order, menu):
    if len(order) == 0:
        print("Your order is empty.")
    else:
        print("Your order is:")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")
    print(f"You have {len(order)} items in your order.")
def calculate_subtotal(order, menu):
   subtotal = 0
   for item in order:
    subtotal += menu[item]
   return subtotal
   print(f"Order Subtotal: ${calculate_subtotal(order, menu):.2f}")
def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        return subtotal * 0.15
    elif is_member and subtotal >= 10:
        return subtotal * 0.10
    elif not is_member and subtotal >= 25:
        return subtotal * 0.05
    else:
        return 0
def print_receipt(name, order, menu, is_member):
   print("*****Python Cafe RECEIPT******")
   subtotal = calculate_subtotal(order, menu)
   discount = get_discount(subtotal, is_member)
   taxable_amount = subtotal - discount
   tax = taxable_amount * tax_rate
   total = taxable_amount + tax
   print(f"Customer: {name}")
   for item in order:
        print(f"{item}: ${menu[item]:.2f}")
   print(f"Subtotal: ${subtotal:.2f}")
   print(f"Discount: -${discount:.2f}")
   print(f"Tax: ${tax:.2f}")
   print(f"Total: ${total:.2f}")
   if not is_member:
        print("Join our Rewards Club today and start earning discounts!")
   print(f"Thanks for visiting {name}!")
def option():
    print("1.View menu")
    print("2.Add an item")
    print("3.Remove an item")
    print("4.View my order")
    print("5.Checkout")
print(cafe_name)
name = input("What's your name: ")
greet(name)
member = input("Are you a rewards member? (yes/no): ")
if member.lower() == "yes":
    is_member = True
else:
    is_member = False
while True:
    option()
    choice = input('Please choose an option (1-5): ')
    if choice == "1":
        show_menu(menu)
    elif choice == "2":
        item = input("What would you like? ").lower()
        quantity = int(input("How many: "))
        for i in range (quantity):
            order.append(item)
        print(f"Added {quantity} {item} to you order!")
    elif choice == "3":
        item = input("Which item should I remove: ")
        order.remove(item)
        print(f"Ok, {item} is removed!")
    elif choice == "4":
        show_order(order,menu)
    elif choice == "5":
        if len(order) == 0:
            print("Please add something to your order first!")
        else: 
             print_receipt(name, order, menu, is_member) 
        break
    else:
        print("Please choose and option between 1-5")
