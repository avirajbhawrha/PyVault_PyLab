"""
main.py - PyVault_PyLab (all 6 tasks merged in ONE file)

Run:  python main.py
Saare tasks ek ke baad ek chalenge aur sab ka log
ek hi file me banega:  logs/logdata.log
"""

import ast
import logging
import os
from datetime import date

# ------------------------------------------------------------------
# COMMON LOGGING SYSTEM (ek hi log file, ek hi jagah)
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "logdata.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("pyvault")


def banner(n, state):
    logger.info(f"-----------------Task {n} {state}--------------------")


# ------------------------------------------------------------------
# TASK 1 - Personal info & data types
# ------------------------------------------------------------------
def task1():
    banner(1, "Started")
    logger.info("Program started.")

    full_name = input("Enter name: ")
    logger.info("Name entered successfully.")

    try:
        age = int(input("Enter age: "))
        logger.info("Age entered successfully.")
    except ValueError:
        logger.error("Invalid age entered. Please enter a number.")
        print("Invalid input! Please enter a valid age.")
        banner(1, "Ended")
        return

    try:
        height = float(input("Enter height: "))
        logger.info("Height entered successfully.")
    except ValueError:
        logger.error("Invalid height entered. Please enter a number.")
        print("Invalid input! Please enter a valid height.")
        banner(1, "Ended")
        return

    favorite_language = input("Enter programming language: ")
    logger.info("Favorite programming language entered.")

    try:
        coding_experience = int(input("Enter experience: "))
        logger.info("Coding experience entered successfully.")
    except ValueError:
        logger.error("Invalid coding experience entered.")
        print("Invalid input! Please enter experience in years as a number.")
        banner(1, "Ended")
        return

    currently_learning_python = True
    logger.info("Currently learning Python: True")

    print("\nPersonal Information")
    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"Height: {height} meters")
    print(f"Favorite Programming Language: {favorite_language}")
    print(f"Years of Coding Experience: {coding_experience}")
    print(f"Currently Learning Python: {currently_learning_python}")

    print("\nData Types")
    print(f"Full Name Type: {type(full_name)}")
    print(f"Age Type: {type(age)}")
    print(f"Height Type: {type(height)}")
    print(f"Favorite Language Type: {type(favorite_language)}")
    print(f"Coding Experience Type: {type(coding_experience)}")
    print(f"Currently Learning Python Type: {type(currently_learning_python)}")

    logger.info("Personal information displayed successfully.")
    logger.info("Data types displayed successfully.")
    logger.info("Program completed successfully.")
    banner(1, "Ended")


# ------------------------------------------------------------------
# TASK 2 - f-Strings sales receipt
# ------------------------------------------------------------------
def task2():
    banner(2, "Started")
    logger.info("Task 2 - f-Strings Practice program started.")

    product_name = input("Enter product name: ")
    logger.info("Product name entered.")

    try:
        price = float(input("Enter price: "))
        logger.info("Price entered.")
        quantity = int(input("Enter quantity: "))
        logger.info("Quantity entered.")
        discount_percentage = float(input("Enter discount percentage: "))
        logger.info("Discount percentage entered.")
    except ValueError:
        logger.error("Invalid number entered in Task 2.")
        print("Invalid input! Please enter numbers only.")
        banner(2, "Ended")
        return

    subtotal = price * quantity
    logger.info(f"Subtotal calculated: {subtotal:.2f}")
    discount_amount = subtotal * discount_percentage / 100
    logger.info(f"Discount amount calculated: {discount_amount:.2f}")
    final_total = subtotal - discount_amount
    logger.info(f"Final total calculated: {final_total:.2f}")

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

    logger.info("Sales receipt displayed successfully.")
    logger.info("Task 2 - f-Strings Practice program completed successfully.")
    banner(2, "Ended")


# ------------------------------------------------------------------
# TASK 3 - Name / birth year / favorite number validation
# ------------------------------------------------------------------
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        cleaned = name.replace(" ", "").replace("-", "")

        if not cleaned.isalpha():
            print("Invalid name. Please use letters only (no numbers or symbols).\n")
            logger.warning(f"Invalid name input: '{name}' (Contains numbers/symbols)")
        elif len(name) > 8:
            print("Name is too long. Maximum allowed length is 8 characters.\n")
            logger.warning(f"Invalid name input: '{name}' (Too long)")
        else:
            logger.info(f"Valid name entered: '{name.title()}'")
            return name.title()


def get_valid_birth_year(current_year):
    while True:
        raw = input("Enter your birth year: ").strip()
        if raw.startswith("-"):
            print("Invalid year. Negative numbers are not allowed.\n")
            logger.warning(f"Invalid year input: '{raw}' (Negative number)")
            continue
        try:
            year = int(raw)
            if 1900 < year <= current_year:
                logger.info(f"Valid birth year entered: {year}")
                return year
            print(f"Invalid year. Must be above 1900 up to {current_year}.\n")
            logger.warning(f"Invalid year input: '{year}' (Out of range)")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit number.\n")
            logger.warning(f"Invalid year input: '{raw}' (Not an integer)")


def get_valid_favorite_number():
    while True:
        raw = input("Enter your favorite number: ").strip()
        if raw.startswith("-"):
            print("Error: Negative numbers are not allowed.\n")
            logger.warning(f"Invalid favorite number input: '{raw}' (Negative number)")
            continue
        try:
            number = int(raw)
            logger.info(f"Valid favorite number entered: {number}")
            return number
        except ValueError:
            print("Please enter a valid number.\n")
            logger.warning(f"Invalid favorite number input: '{raw}' (Not an integer)")


def task3():
    banner(3, "Started")
    logger.info("Program started.")
    current_year = date.today().year

    first_name = get_valid_name("Enter your first name (max 8 letters): ")
    last_name = get_valid_name("Enter your last name (max 8 letters): ")
    birth_year = get_valid_birth_year(current_year)
    favorite_number = get_valid_favorite_number()

    age = current_year - birth_year
    logger.info(f"Calculated age: {age}")

    final_message = (
        f"Full Name: {first_name} {last_name}\n"
        f"Age: {age}\n"
        f"Favorite Number x 2: {favorite_number * 2}"
    )
    print(final_message)

    logger.info(f"Displayed final message to user:\n{final_message}")
    banner(3, "Ended")


# ------------------------------------------------------------------
# TASK 4 - Truthy / Falsy checker
# ------------------------------------------------------------------
def task4():
    banner(4, "Started")
    logger.info("Program started.")

    user_input = input("Enter a value: ")
    logger.info(f"User entered: {user_input}")

    try:
        value = ast.literal_eval(user_input)
        logger.info(f"Input successfully converted to Python value: {value}")
    except (ValueError, SyntaxError):
        value = user_input
        logger.warning("Input could not be evaluated. Treating it as a string.")

    print("Value:", value)
    logger.info(f"Value displayed: {value}")

    if value:
        print("In Python,", value, "is Truthy")
        print("Python checks whether the value is considered present, non-empty, or non-zero.")
        logger.info(f"Value {value} is Truthy.")
    else:
        print("In Python,", value, "is Falsy")
        print("Python checks whether the value is considered empty, zero, absent, or false.")
        logger.info(f"Value {value} is Falsy.")

    logger.info("Program completed successfully.")
    banner(4, "Ended")


# ------------------------------------------------------------------
# TASK 5 - Arithmetic calculator
# ------------------------------------------------------------------
def task5():
    banner(5, "Started")
    logger.info("Calculator started")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        logger.info(f"Numbers entered: {num1}, {num2}")
    except ValueError:
        print("Please enter a number")
        logger.error("Invalid number entered by user")
        banner(5, "Ended")
        return

    operation = input("Enter the operation (+, -, *, /, //, %, **): ").strip()
    logger.info(f"Operation selected: {operation}")

    print("\n--- Arithmetic Operations ---")

    names = {"+": "Addition", "-": "Subtraction", "*": "Multiplication",
             "/": "Division", "//": "Floor division", "%": "Modulus",
             "**": "Exponentiation"}

    if operation not in names:
        print("Invalid operation. Please use one of the following: +, -, *, /, //, %, **")
        logger.warning(f"Invalid operation entered: {operation}")
    elif operation in ("/", "//", "%") and num2 == 0:
        print("Cannot divide by zero")
        logger.error(f"{names[operation]} by zero attempted")
    else:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "//":
            result = num1 // num2
        elif operation == "%":
            result = num1 % num2
        else:
            result = num1 ** num2
        print(f"{num1} {operation} {num2} = {result}")
        logger.info(f"{names[operation]} performed: {num1} {operation} {num2} = {result}")

    logger.info("Calculator execution completed")
    banner(5, "Ended")


# ------------------------------------------------------------------
# TASK 6 - Age, license and eligibility checker
# ------------------------------------------------------------------
def task6():
    banner(6, "Started")
    logger.info("Age eligibility checker started")

    while True:
        try:
            age = int(input("Enter your age: "))
            logger.info(f"Age entered: {age}")
            if age < 18 or age > 105:
                print("Invalid age! Age must be between 18 and 105.")
                logger.warning(f"Invalid age entered: {age}")
            else:
                logger.info(f"Valid age accepted: {age}")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logger.error("Invalid non-numeric age input entered")

    lic = input("Do you have a driver's license? (yes/no): ").strip().lower()
    logger.info(f"License input: {lic}")
    while lic not in ("yes", "no"):
        print("Invalid input! Please enter yes or no.")
        logger.warning(f"Invalid license input: {lic}")
        lic = input("Do you have a driver's license? (yes/no): ").strip().lower()
        logger.info(f"License input: {lic}")

    can_drive = "Yes" if lic == "yes" else "No"
    is_senior = "Yes" if age >= 65 else "No"
    is_teenager = "Yes" if 13 <= age < 20 else "No"
    can_vote = "Yes" if age >= 18 else "No"
    logger.info(f"Can drive: {can_drive}")
    logger.info(f"Senior status: {is_senior}")
    logger.info(f"Teenager status: {is_teenager}")
    logger.info(f"Voting eligibility: {can_vote}")

    print("\n--- Results ---")
    if lic == "yes":
        print("License Status: Has a driver's license")
        logger.info("License status: Has a driver's license")
    else:
        print("License Status: Does not have a driver's license")
        logger.info("License status: Does not have a driver's license")
    print("Can they drive?     ", can_drive)
    print("Are they a senior?  ", is_senior)
    print("Are they a teenager?", is_teenager)
    print("Can they vote?      ", can_vote)

    logger.info("Age eligibility checker completed")
    banner(6, "Ended")


# ------------------------------------------------------------------
# MAIN - saare tasks ek saath
# ------------------------------------------------------------------
def main():
    logger.info("=================== main.py Started ===================")
    for number, task in enumerate([task1, task2, task3, task4, task5, task6], start=1):
        print(f"\n{'=' * 50}\n  TASK {number}\n{'=' * 50}")
        task()
    print("\nAll tasks completed. Log file: logs/logdata.log")
    logger.info("=================== main.py Ended ===================")


if __name__ == "__main__":
    main()