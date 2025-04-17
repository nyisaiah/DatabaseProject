import streamlit as st
from datetime import datetime, time
from backend.customers_backend import get_customers
from backend.appointments_backend import get_ownership, get_tech_to_service, add_appointment, add_job
from backend.technicians_backend import get_technicians
from frontend.utils import format_customer, format_car, format_tech, format_service


def render():
    customer_list = get_customers()
    if 'selected_customer' not in st.session_state:
        st.session_state.selected_customer = None

    if 'selected_ownership' not in st.session_state:
        st.session_state.selected_customer = None

    st.title("🛠️ Create a Mechanic Appointment")
    

    # === STEP 1: Select Customer ===
    st.subheader("Step 1: Select Customer")

   

    selected_customer = st.selectbox("Choose a customer",customer_list, format_func=format_customer)

    st.session_state.selected_customer = selected_customer["cust_id"]

    # === STEP 2: Select Car ===
    st.subheader("Step 2: Select Car")
  
    car_list = get_ownership(selected_customer["cust_id"])
    
    try:
        selected_car = st.selectbox("Choose a car",car_list, format_func=format_car)

        st.session_state.selected_ownership = selected_car['ownership_id']

    except Exception as e:
        st.error('Customer has no cars')
    # === STEP 3: Select Date and Time ===
    st.subheader("Step 3: Select Date and Time")
    appointment_date = st.date_input("Appointment Date", None)
    appointment_time = st.time_input("Appointment Time", time(10,0))
    formatted_time = appointment_time.strftime("%I:%M %p")

    if appointment_time and appointment_date:
            # === STEP 4: Assign Technician and Add Services ===
        st.subheader("Step 4: Assign Technician and Add Services")

        tech_list = get_technicians()


        if "service_list" not in st.session_state:
            st.session_state.service_list = []

        selected_tech = st.selectbox("Select Technician", tech_list, format_func=format_tech)

        if selected_tech:
            tech_id = selected_tech['techid']
            available_services = get_tech_to_service(tech_id)

            if available_services:
                with st.form(key="service_form"):
                    selected_service = st.selectbox("Select a service this tech will do", available_services, format_func=format_service)
                    add_service = st.form_submit_button("➕ Add Service")

                    # Prevent duplicates
                    existing_services = [item["service"] for item in st.session_state.service_list]
                    if add_service:
                        if selected_service in existing_services:
                            st.warning(f"{selected_service['servicename']} already added.")
                        else:
                            st.session_state.service_list.append({
                                "service": selected_service,
                                "mechanic": selected_tech,
                                "id": selected_service['id']
                            })
                            st.success(f"{selected_service['servicename']} added with {format_tech(selected_tech)}")
                            print(selected_service['id'])
            else:
                st.warning("This technician is not assigned to any services.")

        # === Show Services Added with Remove Buttons ===
        if st.session_state.service_list:
            st.write("### Services Added:")
            for idx, item in enumerate(st.session_state.service_list):
                col1, col2, col3 = st.columns([4, 4, 1])
                with col1:
                    st.write(f"{format_service(item['service'])}")
                with col2:
                    st.write(f"Mechanic: {format_tech(item['mechanic'])}")
                with col3:
                    if st.button("❌", key=f"remove_{idx}"):
                        st.session_state.service_list.pop(idx)
                        st.rerun()

        # === STEP 5: Submit Appointment ===
        if selected_customer and selected_car and appointment_date and appointment_time and st.session_state.service_list:
            if st.button("📅 Submit Appointment"):
                try:
                    ownership_id = selected_car['ownership_id']
                    appt_id = add_appointment(appointment_date, appointment_time, ownership_id)
                    print(appt_id)
                    st.success("Appointment submitted!")
                    st.write("**Summary:**")
                    st.write(f"- Customer: {format_customer(selected_customer)}")
                    st.write(f"- Car: {format_car(selected_car)}")
                    st.write(f"- Date: {appointment_date.strftime('%B %d, %Y')}")
                    st.write(f"- Time: {formatted_time}")
                    st.write("**Services:**")
                    try:
                        for item in st.session_state.service_list:
                            job_id = item['id']
                            add_job(appt_id, job_id)
                            st.write(f"• {format_service(item['service'])} (Mechanic: {format_tech(item['mechanic'])})")
                    except Exception as e:
                        st.error(e)
                except Exception as e:
                    st.error(e)

    if st.button("🔁 Start New Appointment"):
        st.session_state.selected_customer = None
        st.session_state.selected_ownership = None
        st.session_state.service_list = []
        st.rerun()