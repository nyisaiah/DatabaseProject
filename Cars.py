import streamlit as st

# State variable to track car form visibility
if "show_car_form" not in st.session_state:
    st.session_state.show_car_form = False

# Button to reveal the new car form
if st.button("Add Car"):
    st.session_state.show_car_form = True

# Show the car form if the button was clicked
if st.session_state.show_car_form:
    with st.form("new_car_form"):
        selected_customer = st.selectbox("Select Car Owner", [], format_func=lambda x: f"{x[0]} - {x[1]}, {x[2]}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            license_plate = st.text_input("License Plate")
        with col2:
            make = st.text_input("Make")
        with col3:
            model = st.text_input("Model")
        
        submit_car_button = st.form_submit_button("Submit New Car")
        
        if submit_car_button:
            st.success("✅ Car added successfully!")
