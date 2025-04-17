import streamlit as st
import pandas as pd
from backend.services_backend import get_services
from backend.technicians_backend import get_technicians, tech_with_service, add_technician
from frontend.utils import format_name, format_service, format_tech

def render():
    st.title("🧑‍🔧 Technicians Page")
    
    if st.button("🔁 Refresh"):
        st.rerun()

    tech_list = get_technicians()
    service_list = get_services()
    st.subheader("🔍 View Technicians")
    if st.button("Load Technicians"):
        df = pd.DataFrame(tech_list)
        df = df.drop(columns=['techid']).rename(columns={'techfname':'First Name','techlname':'Last Name'})
        st.dataframe(df, hide_index=True)

    st.subheader("➕ Add Technician")
    with st.form("add_tech"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        submitted = st.form_submit_button("Add")
        if submitted:
            if first and last:
                first, last = format_name(first), format_name(last)
                try:
                    add_technician(first,last)
                    st.success(f"Successfully added {first} {last} to our database")
                except Exception as e:
                    st.error(e)

    st.subheader("🔗 Associate Technician with Service")

    with st.form("link_tech_service"):
        selected_tech = st.selectbox("Select Technician", tech_list, format_func=format_tech)
        selected_service = st.selectbox("Select Service", service_list, format_func=format_service)
        linked = st.form_submit_button("Link")
        if linked:
            if selected_service and selected_tech:
                try:
                    tech_with_service(selected_tech['techid'], selected_service['serviceid'])
                    st.success(f"Linked {format_service(selected_service)} with {format_tech(selected_tech)}.")
                except Exception as e:
                    st.error(e)