import streamlit as st

def get_age_type(age):
    """Function to determine the age type based on the given age."""
    if age <= 12:
        return "child"
    elif 13 <= age <= 30:
        return "young"
    elif 31 <= age <= 65:
        return "mature"
    else:
        return "tu marra ni abgi tk"

def main():
    """Main function to take input from the user and return age type."""
    st.title("Age Type Detector")
    age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)
    if st.button("Detect Age Type"):
        age_type = get_age_type(age)
        st.write(f"Your age type is: {age_type}")

if __name__ == "__main__":
    main()
