"""
auth.py - Terminal login for PyVault_PyLab

Run:  python auth.py

Login sahi hone ke baad main.py ke saare 6 tasks ek ke baad ek chalte hain.
Login ke attempts bhi usi log file me jaate hain: logs/logdata.log
(password kabhi log me nahi likha jata)
"""

import getpass
import sys

import main  # logging system + saare tasks yahin se aate hain

# ------------------------------------------------------------------
# LOGIN DETAILS (yahan badal sakte ho)
# ------------------------------------------------------------------
USERNAME = "charan"
PASSWORD = "python123"
MAX_ATTEMPTS = 3

logger = main.logger


def login():
    """True return karta hai agar login sahi ho, warna False."""
    print("=" * 50)
    print("        PYTHON PROFILE PORTAL - LOGIN")
    print("=" * 50)
    logger.info("=================== Login Started ===================")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ")

        if username == USERNAME and password == PASSWORD:
            logger.info(f"Login successful for user '{username}'")
            print("\nLogin successful!\n")
            return True

        remaining = MAX_ATTEMPTS - attempt
        logger.warning(f"Failed login attempt {attempt}/{MAX_ATTEMPTS} for username '{username}'")
        if remaining:
            print(f"Invalid username or password. {remaining} attempt(s) left.\n")

    logger.error("Login blocked: too many failed attempts")
    print("Too many failed attempts. Exiting.")
    return False


def run():
    if not login():
        sys.exit(1)
    main.main()  # ab saare 6 tasks queue me chalenge
    logger.info("=================== Logout ===================")


if __name__ == "__main__":
    run()