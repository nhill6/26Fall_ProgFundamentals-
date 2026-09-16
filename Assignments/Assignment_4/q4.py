item = "ball"
unitprice = 5.67
quantity = 10

tax = 0.05

subtotal = unitprice * quantity
taxamount = subtotal * tax
final = subtotal + taxamount

print(f"subtotal: ${subtotal:.2f}")
print(f"Tax amount: ${taxamount:.2f}")
print(f"Final total: ${final:.2f}")
