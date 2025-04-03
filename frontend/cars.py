import streamlit as st

def render():
    st.title("🚗 Cars Page")

    st.subheader("🔍 View Cars")
    if st.button("Load Cars"):
        st.info("Would load all cars and display in a table.")

    st.subheader("➕ Add Car")
    with st.form("add_car"):
        plate = st.text_input("License Plate")
        make = st.text_input("Make")
        model = st.text_input("Model")
        submitted = st.form_submit_button("Add")
        if submitted:
            st.success("Car would be added.")

    st.subheader("🔗 Associate Car with Customer")

    customer_list = ["1: John Doe", "2: Jane Smith"]
    car_list = ["10: ABC123 - Honda Civic", "11: XYZ789 - Toyota Camry"]

    with st.form("link_car_customer"):
        selected_car = st.selectbox("Select Car", car_list)
        selected_customer = st.selectbox("Select Customer", customer_list)
        linked = st.form_submit_button("Link")
        if linked:
            st.success(f"Linked {selected_car} with {selected_customer}.")