import logging

# Configure the logging settings
logging.basicConfig(
    filename='logdata.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("-----------------Task 1 Started--------------------")
logging.info("Program started.")

# Taking input
full_name = input("Enter name: ")
logging.info("Name entered successfully.")

try:
    age = int(input("Enter age: "))
    logging.info("Age entered successfully.")
except ValueError:
    logging.error("Invalid age entered. Please enter a number.")
    print("Invalid input! Please enter a valid age.")
    exit()

try:
    height = float(input("Enter height: "))
    logging.info("Height entered successfully.")
except ValueError:
    logging.error("Invalid height entered. Please enter a number.")
    print("Invalid input! Please enter a valid height.")
    exit()

favorite_language = input("Enter programming language: ")
logging.info("Favorite programming language entered.")

try:
    coding_experience = int(input("Enter experience: "))
    logging.info("Coding experience entered successfully.")
except ValueError:
    logging.error("Invalid coding experience entered.")
    print("Invalid input! Please enter experience in years as a number.")
    exit()

currently_learning_python = True
logging.info("Currently learning Python: True")

# Display Personal Information
print("\nPersonal Information")
print(f"Full Name: {full_name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Favorite Programming Language: {favorite_language}")
print(f"Years of Coding Experience: {coding_experience}")
print(f"Currently Learning Python: {currently_learning_python}")

# Display Data Types
print("\nData Types")
print(f"Full Name Type: {type(full_name)}")
print(f"Age Type: {type(age)}")
print(f"Height Type: {type(height)}")
print(f"Favorite Language Type: {type(favorite_language)}")
print(f"Coding Experience Type: {type(coding_experience)}")
print(f"Currently Learning Python Type: {type(currently_learning_python)}")

# Log successful completion
logging.info("Personal information displayed successfully.")
logging.info("Data types displayed successfully.")
logging.info("Program completed successfully.")
logging.info("-----------------Task 1 Ended--------------------")