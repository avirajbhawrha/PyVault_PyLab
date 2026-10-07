import streamlit as st


# ============================================================
# LOGIN DETAILS
# ============================================================

USERNAME = "charan"
PASSWORD = "python123"


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Python Profile App",
    page_icon="🐍",
    layout="centered"
)


# ============================================================
# LOGIN FUNCTION
# ============================================================

def login_page():

    st.title("🔐 Python Profile Portal")
    st.write("Please login to continue.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state["logged_in"] = True
            st.rerun()

        else:

            st.error("❌ Invalid username or password")


# ============================================================
# PROFILE FUNCTION
# ============================================================

def profile_page():

    st.title("👤 Personal Profile")

    st.success("Login successful!")

    # --------------------------------------------------------
    # Personal Information
    # --------------------------------------------------------

    st.header("Personal Information")

    full_name = st.text_input("Full Name")
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=21
    )

    height = st.number_input(
        "Height (meters)",
        min_value=0.1,
        max_value=3.0,
        value=1.60,
        step=0.01
    )

    favorite_language = st.text_input(
        "Favorite Programming Language"
    )

    coding_experience = st.number_input(
        "Years of Coding Experience",
        min_value=0,
        max_value=50,
        value=1
    )

    currently_learning_python = st.checkbox(
        "Currently Learning Python",
        value=True
    )

    # --------------------------------------------------------
    # Display Profile
    # --------------------------------------------------------

    if st.button("Show Profile"):

        st.divider()

        st.header("📋 Profile Information")

        st.write(f"**Full Name:** {full_name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Height:** {height} meters")
        st.write(
            f"**Favorite Programming Language:** "
            f"{favorite_language}"
        )
        st.write(
            f"**Years of Coding Experience:** "
            f"{coding_experience}"
        )
        st.write(
            f"**Currently Learning Python:** "
            f"{currently_learning_python}"
        )

        st.divider()

        st.subheader("Data Types")

        st.write(
            f"Full Name Type: {type(full_name).__name__}"
        )

        st.write(
            f"Age Type: {type(age).__name__}"
        )

        st.write(
            f"Height Type: {type(height).__name__}"
        )

        st.write(
            f"Favorite Language Type: "
            f"{type(favorite_language).__name__}"
        )

        st.write(
            f"Coding Experience Type: "
            f"{type(coding_experience).__name__}"
        )

        st.write(
            f"Currently Learning Python Type: "
            f"{type(currently_learning_python).__name__}"
        )

    # --------------------------------------------------------
    # Sales Receipt
    # --------------------------------------------------------

    st.divider()

    st.header("🧾 Sales Receipt")

    product_name = st.text_input("Product Name")

    price = st.number_input(
        "Price",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1,
        step=1
    )

    discount_percentage = st.number_input(
        "Discount Percentage",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

    if st.button("Calculate Receipt"):

        # Calculations

        subtotal = price * quantity

        discount_amount = (
            subtotal * discount_percentage / 100
        )

        final_total = (
            subtotal - discount_amount
        )

        # Receipt

        st.divider()

        st.subheader("🧾 SALES RECEIPT")

        st.write(
            f"**Product Name:** {product_name}"
        )

        st.write(
            f"**Unit Price:** ${price:.2f}"
        )

        st.write(
            f"**Quantity:** {quantity}"
        )

        st.write(
            f"**Subtotal:** ${subtotal:.2f}"
        )

        st.write(
            f"**Discount:** "
            f"{discount_percentage:.2f}%"
        )

        st.write(
            f"**Discount Amount:** "
            f"${discount_amount:.2f}"
        )

        st.success(
            f"💰 Final Total: ${final_total:.2f}"
        )

    # --------------------------------------------------------
    # Logout
    # --------------------------------------------------------

    st.divider()

    if st.button("Logout"):

        st.session_state["logged_in"] = False
        st.rerun()


# ============================================================
# MAIN PROGRAM
# ============================================================

if "logged_in" not in st.session_state:

    st.session_state["logged_in"] = False


if st.session_state["logged_in"]:

    profile_page()

else:

    login_page()