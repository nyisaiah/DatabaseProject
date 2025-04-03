from frontend import appointments, reports, customers, cars, services, technicians
import streamlit as st
st.set_page_config(page_title="Mechanic Shop Manager", page_icon="🛠️")

st.sidebar.title("📋 Navigation")
page = st.sidebar.radio("Go to", [
    "Appointments",
    "Customers",
    "Cars",
    "Services",
    "Technicians",
    "Reports"
])

if page == "Appointments":
    appointments.render()
elif page == "Reports":
    reports.render()
elif page == "Customers":
    customers.render()
elif page == "Cars":
    cars.render()
elif page == "Services":
    services.render()
elif page == "Technicians":
    technicians.render()