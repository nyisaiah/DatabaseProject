import streamlit as st
from datetime import date
from backend.reports_backend import get_jobs_for_day, get_services_within_time, get_total_price, get_jobs_for_tech, get_services_for_car, get_techs_no_work
from backend.services_backend import get_services
from backend.technicians_backend import get_technicians
from backend.customers_backend import get_customers
from frontend.utils import format_service, format_tech, format_customer
import pandas as pd

def render():
    st.title("📊 Reports & Queries")
    service_list = get_services()
    tech_list = get_technicians()
    cust_list = get_customers()
    st.markdown("### 📅 Jobs Scheduled for a Given Day")
    job_date = st.date_input("Select a date", value=date.today())
    json_list = get_jobs_for_day(job_date)
    if st.button("Show Jobs for the Day"):
        if json_list:
            df = pd.DataFrame(json_list)
            df['prices'] = df['prices'].apply(lambda x: [f"${item:,.2f}" for item in x])
            st.dataframe(df, hide_index=True)
        else:
            st.warning("No jobs on that day")

    st.markdown("---")
    
    st.markdown("### 🔁 Count of a Given Service Over Time")
    selected_service = st.selectbox("Select Service", service_list, format_func=format_service)
    service_start = st.date_input("Start date", key="service_start")
    service_end = st.date_input("End date", key="service_end")
    json_list = get_services_within_time(selected_service['servicename'],service_start,service_end)
    if st.button("Get Service Count"):
        st.dataframe(json_list)


    st.markdown("---")

    st.markdown("### 💰 Total Cost of All Services During a Time Frame")
    cost_start = st.date_input("Start date", key="cost_start")
    cost_end = st.date_input("End date", key="cost_end")
    total_price = get_total_price(cost_start, cost_end)
    if st.button("Get Total Cost"):
        st.info(f"This time frame will make ${total_price:.2f}")

    st.markdown("---")

    st.markdown("### 🧑‍🔧 Jobs by Technician During Time Range")
    tech = st.selectbox("Select Technician", tech_list, format_func=format_tech)
    tech_start = st.date_input("Start date", key="tech_start")
    tech_end = st.date_input("End date", key="tech_end")
    json_list = get_jobs_for_tech(tech['techid'],tech_start,tech_end)
    if st.button("Show Tech Jobs"):
        if json_list:
            st.dataframe(json_list)
        else:
            st.warning("This Tech has no jobs during this time frame")

    st.markdown("---")

    st.markdown("### 👤 Customer’s Service History Grouped by Car")
    customer = st.selectbox("Enter customer full name", cust_list, format_func=format_customer)
    json_list = get_services_for_car(customer['cust_id'])
    if st.button("Get Customer Service History"):
        if json_list:
            st.dataframe(json_list)
        else:
            st.warning("This Customer has no service history")

    st.markdown("---")

    st.markdown("### 😶 Technicians With No Customers")
    if st.button("List Techs With No Customers"):
        json_list = get_techs_no_work()
        st.dataframe(json_list)

    st.markdown("---")

    st.markdown("### 🧮 Extra Credit: Service % Breakdown by Time Range")
    chart_start = st.date_input("Start date", key="chart_start")
    chart_end = st.date_input("End date", key="chart_end")
    if st.button("Generate Service Breakdown Chart"):
        st.info("Would generate pie chart showing % of each service in selected range.")