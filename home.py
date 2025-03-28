import streamlit as st
import datetime

st.title("Welcome to the Mechanic Shop!")
st.write("Add a new appointment")
st.date_input("Date")
st.time_input("Time", datetime.time(12,00))
pg = st.navigation([st.Page("Customers.py"), 
                    st.Page("Cars.py"),
                    st.Page("Services.py"),
                    st.Page("Technicians.py")])
option = st.selectbox(
    'Select a Customer',
     ('customer1', 'customer2', 'customer3'))

option = st.selectbox(
    'Select a car',
     ('car1', 'car2', 'car3'))

option = st.selectbox(
    'Select a Service',
     ('service1', 'service2', 'service3'))

option = st.selectbox(
    'Select a Technichian',
     ('Tech1', 'Tech2', 'Tech3'))
pg.run()