import streamlit as st
import pandas as pd
from backend.services_backend import get_services, add_service
from backend.technicians_backend import get_technicians, tech_with_service
from frontend.utils import format_name, format_service, format_tech


def render():
    service_list = get_services()
    tech_list = get_technicians()

    st.title("🧾 Services Page")

    st.subheader("🔍 View Services")
    if st.button("Load Services"):
        df = pd.DataFrame(service_list)
        df = df.drop(columns=['serviceid']).rename(
            columns={
            'servicename':'Name',
            'serviceprice':'Price'}).style.format({
            "Price": "${:.2f}"})
        st.dataframe(df, hide_index=True)
        

    st.subheader("➕ Add Service")
    with st.form("add_service"):
        name = st.text_input("Service Name")
        price = st.number_input("Service Price", min_value=0.0, step=1.0)
        submitted = st.form_submit_button("Add")
        if submitted:
            if name and price:
                name = format_name(name)
                try:
                    add_service(name, price)
                    st.success(f"Added new service {name} for {price}")
                except Exception as e:
                    st.error(e)
                
            else:
                st.warning("Must fill out all fields")

    st.subheader("🔗 Associate Service with Technician")

    with st.form("link_service_tech"):
        selected_service = st.selectbox("Select Service", service_list, format_func=format_service)
        selected_tech = st.selectbox("Select Technician", tech_list, format_func=format_tech)
        linked = st.form_submit_button("Link")
        if linked:
            if selected_service and selected_tech:
                try:
                    tech_with_service(selected_tech['techid'], selected_service['serviceid'])
                    st.success(f"Linked {format_service(selected_service)} with {format_tech(selected_tech)}.")
                except Exception as e:
                    st.error(e)