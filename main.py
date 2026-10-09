"""
main.py - PyVault_PyLab (all 6 tasks in one file, for the terminal)

Normal way:   python auth.py   (login first, then this file runs)
Direct run:   python main.py   (no login)

All tasks run one after another and every task writes to the
same log file:  logs/logdata.log
"""

import ast
import logging
import os
import sys
import textwrap
import time
from datetime import date

# ------------------------------------------------------------------
# COMMON LOGGING SYSTEM (one log file, one location)
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
# TASK LOGIC  (no input()/print() - each task returns a list of lines,
#              so the same code works in the terminal and in Streamlit)
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
# QUEUE - all tasks in order 1 -> 6 (app.py uses this too)
# ------------------------------------------------------------------
QUEUE = [
    (1, "Variables and Data Types", task1),
    (2, "f-Strings Practice", task2),
    (3, "User Input and Type Conversions", task3),
    (4, "Truthy and Falsy Values", task4),
    (5, "Arithmetic Operators", task5),
    (6, "Comparison and Logical Operators", task6),
]


TASK_DELAY = 5  # seconds to wait before each next task starts (terminal mode)


def run_queue(inputs, on_start=None, on_done=None, delay=0):
    """
    inputs = {1: {...task1 kwargs}, 2: {...}, ..., 6: {...}}
    Tasks run one after another (delay = wait between tasks, in seconds).
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
    """Keep asking until a valid value is entered."""
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
    """Collect the inputs of all tasks at once (kept for older code)."""
    return {number: COLLECTORS[number]() for number in COLLECTORS}


# ------------------------------------------------------------------
# BOX FORMATTING  (terminal output only)
# ------------------------------------------------------------------
BOX_WIDTH = 60              # total width of the box (characters)
TEXT_WIDTH = BOX_WIDTH - 4  # text width between the border and padding


def box_banner(text):
    """Double-line box with the text centered (the box widens for long text)."""
    inner = max(BOX_WIDTH - 2, len(text) + 4)
    print("\n╔" + "═" * inner + "╗")
    print("║" + text.center(inner) + "║")
    print("╚" + "═" * inner + "╝")


def _is_rule(line):
    """True if the line is only ===== or ----- (a divider line)."""
    stripped = line.strip()
    return len(stripped) >= 10 and set(stripped) <= set("=-")


def box_result(title, lines):
    """Show the result in a single-line box with the title centered on top."""
    top = "┌" + "─" * (BOX_WIDTH - 2) + "┐"
    divider = "├" + "─" * (BOX_WIDTH - 2) + "┤"
    bottom = "└" + "─" * (BOX_WIDTH - 2) + "┘"

    rows = list(lines)
    # drop ===== lines at the start/end, the box border already does that job
    while rows and _is_rule(rows[0]):
        rows.pop(0)
    while rows and _is_rule(rows[-1]):
        rows.pop()

    print(top)
    print("│" + title.center(BOX_WIDTH - 2) + "│")
    print(divider)
    for line in rows:
        if _is_rule(line):
            print(divider)
        elif line.startswith(" " * 10):  # heading like "SALES RECEIPT" -> center it
            print("│ " + line.strip().center(TEXT_WIDTH) + " │")
        else:
            for part in textwrap.wrap(line, TEXT_WIDTH) or [""]:
                print("│ " + part.ljust(TEXT_WIDTH) + " │")
    print(bottom)


def wait_before(number, seconds):
    """Wait before the next task starts, showing a countdown."""
    logger.info(f"Waiting {seconds} sec before Task {number} starts")
    for left in range(seconds, 0, -1):
        print(f"\rTask {number} starts in {left} sec...", end="", flush=True)
        time.sleep(1)
    print("\r" + " " * 40 + "\r", end="", flush=True)


def main():
    """For each task: box banner -> inputs -> box result, waiting TASK_DELAY sec between tasks."""
    try:  # make the box characters display correctly on Windows terminals too
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    logger.info("=================== Task queue Started ===================")

    for number, title, func in QUEUE:
        if number > 1 and TASK_DELAY:
            wait_before(number, TASK_DELAY)

        box_banner(f"TASK {number} ({title})")
        inputs = COLLECTORS[number]()
        lines = func(**inputs)
        print()
        box_result("RESULT", lines)

    logger.info("=================== Task queue Ended ===================")
    print(f"\nAll tasks completed. Log file: {LOG_FILE}")


if __name__ == "__main__":
    main()