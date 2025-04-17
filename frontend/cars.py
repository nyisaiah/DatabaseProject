import streamlit as st
from backend.customers_backend import get_customers, cust_with_car
from backend.cars_backend import get_cars, get_makes, get_models, add_car
from frontend.utils import format_license_plate, format_customer, format_car
import pandas as pd


def render():
    # Globals
    customer_list = get_customers()
    car_list = get_cars()

    if st.button("🔁 Refresh"):
        st.rerun()

    # Track Selected make
    if 'selected_make' not in st.session_state:
        st.session_state.selected_make = None

    st.title("🚗 Cars Page")
    st.subheader("🔍 View Cars")
    
    # Logic to load cars. Used a pandas dataframe
    if st.button("Load Cars"):
        df = pd.DataFrame(car_list)
        df = df.rename(columns={
            "licenseplate": "License Plate",
            "modelname": "Model",
            "makename": "Make"
        }).drop(columns=['car_id', 'modelid', 'makeid'])
        st.dataframe(df, hide_index=True)


    st.subheader("➕ Add Car")

    # Logic to add a car
    plate = st.text_input("License Plate")
    plate = format_license_plate(plate)
    makes  = get_makes()
    selected_make = st.selectbox("Select Make", makes, format_func=lambda x: f'{x['makename']}')
    st.session_state.selected_make = selected_make['makeid']
    models = get_models(selected_make['makeid'])
    selected_model = st.selectbox("Select Model",models, format_func=lambda x: f'{x['modelname']}')
    
    if st.button("Submit"):
        if plate and selected_make and selected_model:
            try:
                add_car(plate,selected_make['makeid'], selected_model['modelid'])
                st.success(f'New {selected_make['makename']} {selected_model['modelname']} added to our database')
            except Exception as e:
                st.error(e)
        else:
            st.warning('Must fill out all fields')


    st.subheader("🔗 Associate Car with Owner")

   
    # Logic to associate car with customer
    with st.form("link_car_customer"):
        selected_car = st.selectbox("Select Car", car_list, format_func=format_car)
        selected_customer = st.selectbox("Select Customer", customer_list, format_func=format_customer)
        linked = st.form_submit_button("Link")
        if linked:
            try: 
                cust_with_car(selected_customer["cust_id"],selected_car["car_id"])
                st.success(f"Linked {format_customer(selected_customer)} with {format_car(selected_car)}.")
            except Exception as e:
                st.error(e)
