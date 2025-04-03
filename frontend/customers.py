import streamlit as st

def render():
    st.title("👥 Customers Page")

    st.subheader("🔍 View Customers")
    if st.button("Load Customers"):
        st.info("Would load all customers and display in a table.")

    st.subheader("➕ Add Customer")
    with st.form("add_customer"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        phone = st.text_input("Phone Number")
        submitted = st.form_submit_button("Add")
        if submitted:
            st.success("Customer would be added.")

    st.subheader("🔗 Associate Customer with Car")

    # Mock dropdown options (replace with real Supabase queries later)
    customer_list = ["1: John Doe", "2: Jane Smith"]
    car_list = ["10: ABC123 - Honda Civic", "11: XYZ789 - Toyota Camry"]

    with st.form("link_customer_car"):
        selected_customer = st.selectbox("Select Customer", customer_list)
        selected_car = st.selectbox("Select Car", car_list)
        linked = st.form_submit_button("Link")
        if linked:
            st.success(f"Linked {selected_customer} with {selected_car}.")