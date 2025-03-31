import streamlit as st

# State variable to track whether the new customer form is shown
if "show_form" not in st.session_state:
    st.session_state.show_form = False

# Button to reveal the new customer form
if st.button("New Customer"):
    st.session_state.show_form = True

# Show the form if the button was clicked
if st.session_state.show_form:
    with st.form("new_customer_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            firstname = st.text_input("First Name")
        with col2:
            lastname = st.text_input("Last Name")
        with col3:
            phone = st.text_input("Phone Number")

        submit_button = st.form_submit_button("Submit New Customer")
        
        if submit_button:
            st.success(f"✅ Customer {firstname} {lastname} added successfully!")
