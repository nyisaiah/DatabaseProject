import streamlit as st
from backend.customers_backend import add_customer, get_customers
import pandas as pd
from  frontend.utils import format_phone, format_customer




def render():
    st.title("👥 Customers Page")
    customer_list = get_customers() 
    st.subheader("🔍 View Customers")
    if st.button("Load Customers"):
            df = pd.DataFrame(customer_list)
            df = df.rename(columns={
            "custid": "Customer ID",
            "custfname": "First Name",
            "custlname": "Last Name",
            "custphonenumber": "Phone Number"
        })
            st.dataframe(df.style.hide(axis="index"))
            

    st.subheader("➕ Add Customer")
    with st.form("add_customer"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        raw_phone = st.text_input("Enter 10-digit phone number", max_chars=10)

        # Validate that it's exactly 10 digits and all numeric
        if raw_phone:
            if raw_phone.isdigit() and len(raw_phone) == 10:
                formatted_phone = format_phone(raw_phone)
        submitted = st.form_submit_button("Add")
        if submitted:
            if formatted_phone and first and last:
                
                try:
                    add_customer(first, last, formatted_phone)
                    st.success(f"{first} {last} added to our database")
                except Exception as e:
                    st.error(e)
            else:
                st.warning("Must fill out all fields")

    st.subheader("🔗 Associate Customer with Car")

    # Mock dropdown options (replace with real Supabase queries later)
    # customer_list = ["1: John Doe", "2: Jane Smith"]
    car_list = ["10: ABC123 - Honda Civic", "11: XYZ789 - Toyota Camry"]

    with st.form("link_customer_car"):
        selected_customer = st.selectbox("Select Customer", customer_list, format_func=format_customer)
        print(selected_customer["cust_id"])
        selected_car = st.selectbox("Select Car", car_list)
        linked = st.form_submit_button("Link")
        if linked:
            st.success(f"Linked {format_customer(selected_customer)} with {selected_car}.")