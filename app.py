import streamlit as st

def square_value(value):
    """Function to return the square of a value."""
    return value ** 2

def main():
    """Main function to take input from the user and return the square."""
    st.title("Square Calculator")
    num = st.number_input("Enter a number:")
    if st.button("Calculate"):
        result = square_value(num)
        st.write(f"The square of {num} is {result}.")

if __name__ == "__main__":
    main()
