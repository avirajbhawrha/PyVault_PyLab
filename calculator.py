# TASK-5 Arithmetic Operators - Simple Math Calculator

import logging

# Configure logging
logging.basicConfig(
    filename="logdata.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("-----------------Task 5 Started---------------------")
logger.info("Calculator started")

# Take two numbers from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    logger.info(f"Numbers entered: {num1}, {num2}")

except ValueError:
    print("Please enter a number")
    logger.error("Invalid number entered by user")
    exit()

# Take the operation from the user
operation = input("Enter the operation (+, -, *, /, //, %, **): ")

logger.info(f"Operation selected: {operation}")

print("\n--- Arithmetic Operations ---")

# Addition
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    logger.info(f"Addition performed: {num1} + {num2} = {result}")

# Subtraction
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    logger.info(f"Subtraction performed: {num1} - {num2} = {result}")

# Multiplication
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    logger.info(f"Multiplication performed: {num1} * {num2} = {result}")

# Division
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
        logger.info(f"Division performed: {num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero")
        logger.error("Division by zero attempted")

# Floor Division
elif operation == '//':
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
        logger.info(f"Floor division performed: {num1} // {num2} = {result}")
    else:
        print("Cannot divide by zero")
        logger.error("Floor division by zero attempted")

# Modulus
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
        logger.info(f"Modulus performed: {num1} % {num2} = {result}")
    else:
        print("Cannot divide by zero")
        logger.error("Modulus by zero attempted")

# Exponentiation
elif operation == '**':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
    logger.info(f"Exponentiation performed: {num1} ** {num2} = {result}")

# Invalid operation
else:
    print("Invalid operation. Please use one of the following: +, -, *, /, //, %, **")
    logger.warning(f"Invalid operation entered: {operation}")

logger.info("Calculator execution completed")
logger.info("-----------------Task 5 Ended--------------------")