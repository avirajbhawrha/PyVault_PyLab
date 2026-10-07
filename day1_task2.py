# Task 2: f-Strings Practice

# Taking input from user
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))

# Calculations
subtotal = price * quantity
discount_amount = subtotal * discount_percentage / 100
final_total = subtotal - discount_amount

# Display formatted receipt
print("\n" + "=" * 45)
print("              SALES RECEIPT")
print("=" * 45)git switch -c task-day-2


print(f"Product Name       : {product_name}")
print(f"Unit Price         : ${price:.2f}")
print(f"Quantity           : {quantity}")
print("-" * 45)
print(f"Subtotal           : ${subtotal:.2f}")
print(f"Discount           : {discount_percentage:.2f}%")
print(f"Discount Amount    : ${discount_amount:.2f}")
print("-" * 45)
print(f"Final Total        : ${final_total:.2f}")
print("=" * 45)