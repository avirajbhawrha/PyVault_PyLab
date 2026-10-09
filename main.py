"""
main.py - PyVault_PyLab (saare 6 tasks ek file me, terminal ke liye)

Normal tareeka:   python auth.py   (pehle login, phir yeh file chalti hai)
Seedha chalana:   python main.py   (bina login ke)

Saare tasks ek ke baad ek chalte hain aur sabka log
ek hi file me banta hai:  logs/logdata.log
"""

import ast
import logging
import os
import time
from datetime import date

# ------------------------------------------------------------------
# COMMON LOGGING SYSTEM (ek hi log file, ek hi jagah)
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "logdata.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("pyvault")


def banner(n, state):
    logger.info(f"-----------------Task {n} {state}--------------------")


# ------------------------------------------------------------------
# VALIDATORS  ->  (ok, cleaned_value_or_error_message)
# ------------------------------------------------------------------
def validate_name(name):
    name = str(name).strip()
    cleaned = name.replace(" ", "").replace("-", "")
    if not cleaned.isalpha():
        logger.warning(f"Invalid name input: '{name}' (Contains numbers/symbols)")
        return False, "Invalid name. Please use letters only (no numbers or symbols)."
    if len(name) > 8:
        logger.warning(f"Invalid name input: '{name}' (Too long)")
        return False, "Name is too long. Maximum allowed length is 8 characters."
    logger.info(f"Valid name entered: '{name.title()}'")
    return True, name.title()


def validate_birth_year(raw):
    raw = str(raw).strip()
    current_year = date.today().year
    if raw.startswith("-"):
        logger.warning(f"Invalid year input: '{raw}' (Negative number)")
        return False, "Invalid year. Negative numbers are not allowed."
    try:
        year = int(raw)
    except ValueError:
        logger.warning(f"Invalid year input: '{raw}' (Not an integer)")
        return False, "Invalid input. Please enter a valid 4-digit number."
    if not 1900 < year <= current_year:
        logger.warning(f"Invalid year input: '{year}' (Out of range)")
        return False, f"Invalid year. Must be above 1900 up to {current_year}."
    logger.info(f"Valid birth year entered: {year}")
    return True, year


def validate_favorite_number(raw):
    raw = str(raw).strip()
    if raw.startswith("-"):
        logger.warning(f"Invalid favorite number input: '{raw}' (Negative number)")
        return False, "Error: Negative numbers are not allowed."
    try:
        number = int(raw)
    except ValueError:
        logger.warning(f"Invalid favorite number input: '{raw}' (Not an integer)")
        return False, "Please enter a valid number."
    logger.info(f"Valid favorite number entered: {number}")
    return True, number


# ------------------------------------------------------------------
# TASK LOGIC  (koi input()/print() nahi - lines ki list return karte hain,
#              isliye terminal aur Streamlit dono me chalte hain)
# ------------------------------------------------------------------
def task1(full_name, age, height, favorite_language, coding_experience):
    banner(1, "Started")
    logger.info("Program started.")
    logger.info("Name entered successfully.")
    logger.info("Age entered successfully.")
    logger.info("Height entered successfully.")
    logger.info("Favorite programming language entered.")
    logger.info("Coding experience entered successfully.")

    learning = True
    logger.info("Currently learning Python: True")

    lines = [
        "Personal Information",
        f"Full Name: {full_name}",
        f"Age: {age}",
        f"Height: {height} meters",
        f"Favorite Programming Language: {favorite_language}",
        f"Years of Coding Experience: {coding_experience}",
        f"Currently Learning Python: {learning}",
        "",
        "Data Types",
        f"Full Name Type: {type(full_name)}",
        f"Age Type: {type(age)}",
        f"Height Type: {type(height)}",
        f"Favorite Language Type: {type(favorite_language)}",
        f"Coding Experience Type: {type(coding_experience)}",
        f"Currently Learning Python Type: {type(learning)}",
    ]
    logger.info("Personal information displayed successfully.")
    logger.info("Data types displayed successfully.")
    logger.info("Program completed successfully.")
    banner(1, "Ended")
    return lines


def task2(product_name, price, quantity, discount_percentage):
    banner(2, "Started")
    logger.info("Task 2 - f-Strings Practice program started.")
    logger.info("Product name entered.")
    logger.info("Price entered.")
    logger.info("Quantity entered.")
    logger.info("Discount percentage entered.")

    subtotal = price * quantity
    logger.info(f"Subtotal calculated: {subtotal:.2f}")
    discount_amount = subtotal * discount_percentage / 100
    logger.info(f"Discount amount calculated: {discount_amount:.2f}")
    final_total = subtotal - discount_amount
    logger.info(f"Final total calculated: {final_total:.2f}")

    lines = [
        "=" * 45,
        "              SALES RECEIPT",
        "=" * 45,
        f"Product Name       : {product_name}",
        f"Unit Price         : ${price:.2f}",
        f"Quantity           : {quantity}",
        "-" * 45,
        f"Subtotal           : ${subtotal:.2f}",
        f"Discount           : {discount_percentage:.2f}%",
        f"Discount Amount    : ${discount_amount:.2f}",
        "-" * 45,
        f"Final Total        : ${final_total:.2f}",
        "=" * 45,
    ]
    logger.info("Sales receipt displayed successfully.")
    logger.info("Task 2 - f-Strings Practice program completed successfully.")
    banner(2, "Ended")
    return lines


def task3(first_name, last_name, birth_year, favorite_number):
    banner(3, "Started")
    logger.info("Program started.")

    checks = [
        validate_name(first_name),
        validate_name(last_name),
        validate_birth_year(birth_year),
        validate_favorite_number(favorite_number),
    ]
    for ok, value in checks:
        if not ok:
            banner(3, "Ended")
            return [f"Error: {value}"]

    first, last, year, fav = (c[1] for c in checks)
    age = date.today().year - year
    logger.info(f"Calculated age: {age}")

    lines = [
        f"Full Name: {first} {last}",
        f"Age: {age}",
        f"Favorite Number x 2: {fav * 2}",
    ]
    logger.info("Displayed final message to user:\n" + "\n".join(lines))
    banner(3, "Ended")
    return lines


def task4(user_input):
    banner(4, "Started")
    logger.info("Program started.")
    logger.info(f"User entered: {user_input}")

    try:
        value = ast.literal_eval(user_input)
        logger.info(f"Input successfully converted to Python value: {value}")
    except (ValueError, SyntaxError):
        value = user_input
        logger.warning("Input could not be evaluated. Treating it as a string.")

    lines = [f"Value: {value}"]
    logger.info(f"Value displayed: {value}")

    if value:
        lines += [f"In Python, {value} is Truthy",
                  "Python checks whether the value is considered present, non-empty, or non-zero."]
        logger.info(f"Value {value} is Truthy.")
    else:
        lines += [f"In Python, {value} is Falsy",
                  "Python checks whether the value is considered empty, zero, absent, or false."]
        logger.info(f"Value {value} is Falsy.")

    logger.info("Program completed successfully.")
    banner(4, "Ended")
    return lines


OPERATIONS = {"+": "Addition", "-": "Subtraction", "*": "Multiplication",
              "/": "Division", "//": "Floor division", "%": "Modulus",
              "**": "Exponentiation"}


def task5(num1, num2, operation):
    banner(5, "Started")
    logger.info("Calculator started")
    logger.info(f"Numbers entered: {num1}, {num2}")
    logger.info(f"Operation selected: {operation}")

    lines = ["--- Arithmetic Operations ---"]

    if operation not in OPERATIONS:
        lines.append("Invalid operation. Please use one of the following: +, -, *, /, //, %, **")
        logger.warning(f"Invalid operation entered: {operation}")
    elif operation in ("/", "//", "%") and num2 == 0:
        lines.append("Cannot divide by zero")
        logger.error(f"{OPERATIONS[operation]} by zero attempted")
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
        lines.append(f"{num1} {operation} {num2} = {result}")
        logger.info(f"{OPERATIONS[operation]} performed: {num1} {operation} {num2} = {result}")

    logger.info("Calculator execution completed")
    banner(5, "Ended")
    return lines


def task6(age, license_answer):
    banner(6, "Started")
    logger.info("Age eligibility checker started")
    logger.info(f"Age entered: {age}")

    lic = str(license_answer).strip().lower()
    if age < 18 or age > 105:
        logger.warning(f"Invalid age entered: {age}")
        banner(6, "Ended")
        return ["Invalid age! Age must be between 18 and 105."]
    if lic not in ("yes", "no"):
        logger.warning(f"Invalid license input: {lic}")
        banner(6, "Ended")
        return ["Invalid input! Please enter yes or no."]

    logger.info(f"Valid age accepted: {age}")
    logger.info(f"License input: {lic}")

    can_drive = "Yes" if lic == "yes" else "No"
    is_senior = "Yes" if age >= 65 else "No"
    is_teenager = "Yes" if 13 <= age < 20 else "No"
    can_vote = "Yes" if age >= 18 else "No"
    logger.info(f"Can drive: {can_drive}")
    logger.info(f"Senior status: {is_senior}")
    logger.info(f"Teenager status: {is_teenager}")
    logger.info(f"Voting eligibility: {can_vote}")

    status = "Has a driver's license" if lic == "yes" else "Does not have a driver's license"
    logger.info(f"License status: {status}")

    lines = [
        "--- Results ---",
        f"License Status: {status}",
        f"Can they drive?      {can_drive}",
        f"Are they a senior?   {is_senior}",
        f"Are they a teenager? {is_teenager}",
        f"Can they vote?       {can_vote}",
    ]
    logger.info("Age eligibility checker completed")
    banner(6, "Ended")
    return lines


# ------------------------------------------------------------------
# QUEUE - saare tasks 1 -> 6 order me (app.py yahi use karta hai)
# ------------------------------------------------------------------
QUEUE = [
    (1, "Personal Info & Data Types", task1),
    (2, "Sales Receipt (f-Strings)", task2),
    (3, "Name / Birth Year Validation", task3),
    (4, "Truthy / Falsy Checker", task4),
    (5, "Arithmetic Calculator", task5),
    (6, "Age & License Checker", task6),
]


TASK_DELAY = 5  # seconds to wait before each next task starts (terminal mode)


def run_queue(inputs, on_start=None, on_done=None, delay=0):
    """
    inputs = {1: {...task1 kwargs}, 2: {...}, ..., 6: {...}}
    Tasks ek ke baad ek chalte hain (delay = tasks ke beech ka wait, seconds).
    Return: [(number, title, lines), ...]
    """
    logger.info("=================== Task queue Started ===================")
    results = []
    for number, title, func in QUEUE:
        if number > 1 and delay:
            time.sleep(delay)
        if on_start:
            on_start(number, title)
        lines = func(**inputs[number])
        results.append((number, title, lines))
        if on_done:
            on_done(number, title, lines)
    logger.info("=================== Task queue Ended ===================")
    return results


# ------------------------------------------------------------------
# TERMINAL MODE  (python main.py)
# ------------------------------------------------------------------
def ask(prompt, cast=str):
    """Sahi value milne tak dobara poochta hai."""
    while True:
        raw = input(prompt)
        try:
            return cast(raw)
        except ValueError:
            print("Invalid input! Please try again.\n")
            logger.warning(f"Invalid input for '{prompt.strip()}': {raw!r}")


def ask_valid(prompt, validator):
    while True:
        ok, value = validator(input(prompt))
        if ok:
            return value
        print(value + "\n")


def collect_task1():
    return dict(
        full_name=input("Enter name: "),
        age=ask("Enter age: ", int),
        height=ask("Enter height: ", float),
        favorite_language=input("Enter programming language: "),
        coding_experience=ask("Enter experience: ", int),
    )


def collect_task2():
    return dict(
        product_name=input("Enter product name: "),
        price=ask("Enter price: ", float),
        quantity=ask("Enter quantity: ", int),
        discount_percentage=ask("Enter discount percentage: ", float),
    )


def collect_task3():
    return dict(
        first_name=ask_valid("Enter your first name (max 8 letters): ", validate_name),
        last_name=ask_valid("Enter your last name (max 8 letters): ", validate_name),
        birth_year=ask_valid("Enter your birth year: ", validate_birth_year),
        favorite_number=ask_valid("Enter your favorite number: ", validate_favorite_number),
    )


def collect_task4():
    return dict(user_input=input("Enter a value: "))


def collect_task5():
    return dict(
        num1=ask("Enter the first number: ", float),
        num2=ask("Enter the second number: ", float),
        operation=input("Enter the operation (+, -, *, /, //, %, **): ").strip(),
    )


def collect_task6():
    while True:
        age = ask("Enter your age: ", int)
        if 18 <= age <= 105:
            break
        print("Invalid age! Age must be between 18 and 105.")
    while True:
        lic = input("Do you have a driver's license? (yes/no): ").strip().lower()
        if lic in ("yes", "no"):
            break
        print("Invalid input! Please enter yes or no.")
    return dict(age=age, license_answer=lic)


COLLECTORS = {1: collect_task1, 2: collect_task2, 3: collect_task3,
              4: collect_task4, 5: collect_task5, 6: collect_task6}


def collect_terminal_inputs():
    """Saare tasks ke inputs ek saath (purane code ke liye)."""
    return {number: COLLECTORS[number]() for number in COLLECTORS}


def wait_before(number, seconds):
    """Next task shuru hone se pehle seconds tak ruko (countdown ke saath)."""
    logger.info(f"Waiting {seconds} sec before Task {number} starts")
    for left in range(seconds, 0, -1):
        print(f"\rTask {number} starts in {left} sec...", end="", flush=True)
        time.sleep(1)
    print("\r" + " " * 40 + "\r", end="", flush=True)


def main():
    """Har task: banner -> inputs -> result. Tasks ke beech TASK_DELAY sec wait."""
    logger.info("=================== Task queue Started ===================")

    for number, title, func in QUEUE:
        if number > 1 and TASK_DELAY:
            wait_before(number, TASK_DELAY)

        print(f"\n{'=' * 50}\n  TASK {number}\n{'=' * 50}")
        inputs = COLLECTORS[number]()
        lines = func(**inputs)
        print("\n" + "\n".join(lines))

    logger.info("=================== Task queue Ended ===================")
    print(f"\nAll tasks completed. Log file: {LOG_FILE}")


if __name__ == "__main__":
    main()