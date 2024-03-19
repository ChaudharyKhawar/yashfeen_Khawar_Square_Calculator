import streamlit as st
import math

def calculate_quadratic(a, b, c):
    """Function to calculate the roots of a quadratic equation."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def main():
    """Main function to take input from the user and calculate the roots."""
    st.title("Quadratic Equation Solver")
    a = st.number_input("Enter the value of a:")
    b = st.number_input("Enter the value of b:")
    c = st.number_input("Enter the value of c:")
    if st.button("Calculate"):
        root1, root2 = calculate_quadratic(a, b, c)
        st.write("Root 1:", root1)
        st.write("Root 2:", root2)

if __name__ == "__main__":
    main()
