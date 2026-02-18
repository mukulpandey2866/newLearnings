# pname = input("Enter your name: ")
# print("Hello", pname)  # this will print "Hello" followed by the value of


pname = input("Enter product name: ")
price = float(input("Enter Price: ")) # We conver to float because it treats as string otherwise
qty = int(input("Enter Quantity: "))
discount = float(input("Enter Discount: "))
# total = price * qty
total_after_discount = price * qty - discount
print(f"Product Name: {pname}")
print("Product Name: ", pname)
print("Price: ", price )
print("Quantity: ", qty)
print("Discount: ", discount)
print(f"Total after discount: {total_after_discount:.2f}")

