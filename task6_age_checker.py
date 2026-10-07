# TASK - Age, License and Eligibility Checker

import logging

# Configure logging
logging.basicConfig(
    filename="task5_6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Age eligibility checker started")

# Get valid age
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

# Check driver's license
if age >= 18:
    license = input("Do you have a driver's license? (yes/no): ").lower()

    logger.info(f"License input: {license}")

    while license != "yes" and license != "no":
        print("Invalid input! Please enter yes or no.")
        logger.warning(f"Invalid license input: {license}")

        license = input(
            "Do you have a driver's license? (yes/no): "
        ).lower()

        logger.info(f"License input: {license}")

    can_drive = "Yes" if license == "yes" else "No"

    logger.info(f"Can drive: {can_drive}")

else:
    license = "no"
    can_drive = "No"

# Age-based checks
is_senior = "Yes" if age >= 65 else "No"
is_teenager = "Yes" if age >= 13 and age < 20 else "No"
can_vote = "Yes" if age >= 18 else "No"

logger.info(f"Senior status: {is_senior}")
logger.info(f"Teenager status: {is_teenager}")
logger.info(f"Voting eligibility: {can_vote}")

# Display results
print("\n--- Results ---")

if age < 18 or age > 50:
    print("License Status: Not eligible to hold a driver's license.")
    logger.info("License status: Not eligible")
else:
    if license == "yes":
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