import streamlit as st
from datetime import datetime

def calculate_age(birth_date):
    """Function to calculate age based on the provided birth date."""
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    """Main function to take input from the user and calculate age."""
    st.title("Age Calculator")
    birth_date = st.date_input("Enter your date of birth:")
    if st.button("Calculate Age"):
        age = calculate_age(birth_date)
        st.write(f"Your age is {age} years.")

if __name__ == "__main__":
    main()
