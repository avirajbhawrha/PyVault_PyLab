import logging

# Configure the logging settings
logging.basicConfig(
    filename='logdata.log',  # The file where logs will be stored
    level=logging.INFO,              # Log level (INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s', # Include timestamp
    datefmt='%Y-%m-%d %H:%M:%S'      # Format for the timestamp
)
logging.info("-----------------Task 3 Started--------------------")
logging.info("Program started.")

# Helper function to validate names (letters only, max 8 characters)
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        cleaned = name.replace(" ", "").replace("-", "")
        
        if not cleaned.isalpha():
            msg = "Invalid name. Please use letters only (no numbers or symbols)."
            print(msg + "\n")
            logging.warning(f"Invalid name input: '{name}' (Contains numbers/symbols)")
        elif len(name) > 8:
            msg = "Name is too long. Maximum allowed length is 8 characters."
            print(msg + "\n")
            logging.warning(f"Invalid name input: '{name}' (Too long)")
        else:
            logging.info(f"Valid name entered: '{name.title()}'")
            return name.title()

# Helper function to validate birth year (between 1901 and 2024)
def get_valid_birth_year():
    while True:
        raw_input = input("Enter your birth year: ").strip()
        if raw_input.startswith("-"):
            msg = "Invalid year. Negative numbers are not allowed."
            print(msg + "\n")
            logging.warning(f"Invalid year input: '{raw_input}' (Negative number)")
            continue
        try:
            year = int(raw_input)
            if 1900 < year <= 2024:
                logging.info(f"Valid birth year entered: {year}")
                return year
            msg = "Invalid year. Must be above 1900 up to 2024."
            print(msg + "\n")
            logging.warning(f"Invalid year input: '{year}' (Out of range)")
        except ValueError:
            msg = "Invalid input. Please enter a valid 4-digit number."
            print(msg + "\n")
            logging.warning(f"Invalid year input: '{raw_input}' (Not an integer)")

# Helper function to get favorite number (rejects negative numbers)
def get_valid_favorite_number():
    while True:
        raw_input = input("Enter your favorite number: ").strip()
        if raw_input.startswith("-"):
            msg = "Error: Negative numbers are not allowed."
            print(msg + "\n")
            logging.warning(f"Invalid favorite number input: '{raw_input}' (Negative number)")
            continue
        try:
            number = int(raw_input)
            logging.info(f"Valid favorite number entered: {number}")
            return number
        except ValueError:
            msg = "Please enter a valid number."
            print(msg + "\n")
            logging.warning(f"Invalid favorite number input: '{raw_input}' (Not an integer)")

# --- Main Program Execution ---

logging.info("--- Program Started ---")

# 1. Ask for validated names (max 8 chars each)
first_name = get_valid_name("Enter your first name (max 8 letters): ")
last_name = get_valid_name("Enter your last name (max 8 letters): ")

# 2. Ask for validated birth year and favorite number
birth_year = get_valid_birth_year()
favorite_number = get_valid_favorite_number()

# 3. Calculate age
age = 2024 - birth_year
logging.info(f"Calculated age: {age}")

# 4. Display personalized message
final_message = (
    f"Full Name: {first_name} {last_name}\n"
    f"Age: {age}\n"
    f"Favorite Number × 2: {favorite_number * 2}"
)

print(final_message)


# Log the final output
logging.info(f"Displayed final message to user:\n{final_message}")
logging.info("--- task 3 Finished ---\n")