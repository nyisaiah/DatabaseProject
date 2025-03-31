import streamlit as st

st.title("Add a New Technician")
if "show_technician_form" not in st.session_state:
    st.session_state.show_technician_form = False

if st.button("New Technician"):
    st.session_state.show_technician_form = True

if st.session_state.show_technician_form:
    with st.form("new_technician_form"):
        tech_fn = st.text_input("First Name")
        tech_ln = st.text_input("Last Name")
        
        submit_technician = st.form_submit_button("Submit New Technician")
        if submit_technician:
            st.success(f"✅ Technician {tech_fn} {tech_ln} added successfully!")
