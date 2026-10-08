# Task 2: f-Strings Practice with Logging

import logging

# Configure the logging settings
logging.basicConfig(
    filename='task2.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info("-----------------Task 2 Started--------------------")
logging.info("Program started.")

# Log program start
logging.info("Task 2 - f-Strings Practice program started.")

# Taking input from user
product_name = input("Enter product name: ")
logging.info("Product name entered.")

price = float(input("Enter price: "))
logging.info("Price entered.")

quantity = int(input("Enter quantity: "))
logging.info("Quantity entered.")

discount_percentage = float(input("Enter discount percentage: "))
logging.info("Discount percentage entered.")

# Calculations
subtotal = price * quantity
logging.info(f"Subtotal calculated: {subtotal:.2f}")

discount_amount = subtotal * discount_percentage / 100
logging.info(f"Discount amount calculated: {discount_amount:.2f}")

final_total = subtotal - discount_amount
logging.info(f"Final total calculated: {final_total:.2f}")

# Display formatted receipt
print("\n" + "=" * 45)
print("              SALES RECEIPT")
print("=" * 45)

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

# Log successful completion
logging.info("Sales receipt displayed successfully.")
logging.info("Task 2 - f-Strings Practice program completed successfully.")
logging.info("----------------Task 4 Ended-------------------")