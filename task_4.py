import ast
import logging

# Configure the logging settings
logging.basicConfig(
    filename='logdata.log',  # The file where logs will be stored
    level=logging.INFO,      # Log level (INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info("-----------------Task 1 Started--------------------")
logging.info("Program started.")

# Log program start
logging.info("Program started.")

# Take input from user
user_input = input("Enter a value: ")
logging.info(f"User entered: {user_input}")

# Convert input into Python value
try:
    value = ast.literal_eval(user_input)
    logging.info(f"Input successfully converted to Python value: {value}")

except (ValueError, SyntaxError):
    value = user_input
    logging.warning("Input could not be evaluated. Treating it as a string.")

# Display value
print("Value:", value)
logging.info(f"Value displayed: {value}")

# Check Truthy or Falsy
if value:
    print("In Python,", value, "is Truthy")
    print("Python checks whether the value is considered present, non-empty, or non-zero.")

    logging.info(f"Value {value} is Truthy.")

else:
    print("In Python,", value, "is Falsy")
    print("Python checks whether the value is considered empty, zero, absent, or false.")

    logging.info(f"Value {value} is Falsy.")

# Log program completion
logging.info("Program completed successfully.")
logging.info("----------------Task 4 Ended-------------------")