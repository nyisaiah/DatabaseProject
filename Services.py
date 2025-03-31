import streamlit as st

st.title("Add a New Service")
if "show_service_form" not in st.session_state:
    st.session_state.show_service_form = False

if st.button("New Service"):
    st.session_state.show_service_form = True

if st.session_state.show_service_form:
    with st.form("new_service_form"):
        service_name = st.text_input("Service Name")
        cost = st.number_input("Cost", min_value=0.0, format="%.2f")
        
        submit_service = st.form_submit_button("Submit New Service")
        if submit_service:
            st.success(f"✅ Service '{service_name}' added successfully!")
