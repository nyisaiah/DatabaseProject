import streamlit as st
from datetime import date

def render():
    st.title("📊 Reports & Queries")

    st.markdown("### 📅 Jobs Scheduled for a Given Day")
    job_date = st.date_input("Select a date", value=date.today())
    if st.button("Show Jobs for the Day"):
        st.info("Would display all jobs, with customer, tech, car, and cost details.")

    st.markdown("---")
    
    st.markdown("### 🔁 Count of a Given Service Over Time")
    service_name = st.selectbox("Select service", ["Oil Change", "Tire Rotation", "Brake Inspection"])
    service_start = st.date_input("Start date", key="service_start")
    service_end = st.date_input("End date", key="service_end")
    if st.button("Get Service Count"):
        st.info("Would display how many of this service were performed in selected time range.")

    st.markdown("---")

    st.markdown("### 💰 Total Cost of All Services During a Time Frame")
    cost_start = st.date_input("Start date", key="cost_start")
    cost_end = st.date_input("End date", key="cost_end")
    if st.button("Get Total Cost"):
        st.info("Would display total cost of all services during time frame.")

    st.markdown("---")

    st.markdown("### 🧑‍🔧 Jobs by Technician During Time Range")
    tech_name = st.selectbox("Select technician", ["Mike", "Linda", "Carlos"])
    tech_start = st.date_input("Start date", key="tech_start")
    tech_end = st.date_input("End date", key="tech_end")
    if st.button("Show Tech Jobs"):
        st.info("Would list each job that tech is doing with car and owner info.")

    st.markdown("---")

    st.markdown("### 👤 Customer’s Service History Grouped by Car")
    customer_name = st.text_input("Enter customer full name")
    if st.button("Get Customer Service History"):
        st.info("Would show grouped services by each car owned by the customer.")

    st.markdown("---")

    st.markdown("### 😶 Technicians With No Customers")
    if st.button("List Techs With No Customers"):
        st.info("Would list names of all technicians not assigned to any customer/job.")

    st.markdown("---")

    st.markdown("### 🧮 Extra Credit: Service % Breakdown by Time Range")
    chart_start = st.date_input("Start date", key="chart_start")
    chart_end = st.date_input("End date", key="chart_end")
    if st.button("Generate Service Breakdown Chart"):
        st.info("Would generate pie chart showing % of each service in selected range.")