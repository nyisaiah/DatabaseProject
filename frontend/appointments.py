import streamlit as st
from datetime import datetime, time

def render():
    st.title("🛠️ Create a Mechanic Appointment")

    # === STEP 1: Select Customer ===
    st.subheader("Step 1: Select Customer")
    # Placeholder customer data
    customers = [
        {"id": 1, "first_name": "John", "last_name": "Doe"},
        {"id": 2, "first_name": "Jane", "last_name": "Smith"},
    ]

    customer_options = [f"{c['id']}: {c['first_name']} {c['last_name']}" for c in customers]
    selected_customer = st.selectbox("Choose a customer", customer_options)

    # === STEP 2: Select Car ===
    st.subheader("Step 2: Select Car")
    # Placeholder car data
    cars = [
        {"id": 1, "plate": "ABC123", "make": "Toyota", "model": "Camry"},
        {"id": 2, "plate": "XYZ789", "make": "Honda", "model": "Civic"},
    ]

    car_options = [f"{c['id']}: {c['plate']} - {c['make']} {c['model']}" for c in cars]
    selected_car = st.selectbox("Choose a car", car_options)

    # === STEP 3: Select Date and Time ===
    st.subheader("Step 3: Select Date and Time")

    # Separate date and time inputs
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time", value=time(10, 0))  # 10:00 AM default

    # Format time for display (12-hour AM/PM format)
    formatted_time = appointment_time.strftime("%I:%M %p")

    # === STEP 4: Add Services and Mechanics ===
    st.subheader("Step 4: Add Services")

    # Placeholder services and mechanics
    services = ["Oil Change", "Tire Rotation", "Brake Inspection"]
    mechanics = ["Mike", "Linda", "Carlos"]

    if "service_list" not in st.session_state:
        st.session_state.service_list = []

    with st.form(key="service_form"):
        selected_service = st.selectbox("Choose a service", services)
        selected_mechanic = st.selectbox("Assign a mechanic", mechanics)
        add_service = st.form_submit_button("➕ Add Service")

        if add_service:
            st.session_state.service_list.append({
                "service": selected_service,
                "mechanic": selected_mechanic
            })

    # Display current list of services added
    if st.session_state.service_list:
        st.write("### Services Added:")
        for idx, item in enumerate(st.session_state.service_list, start=1):
            st.write(f"{idx}. {item['service']} - {item['mechanic']}")

    # === STEP 5: Submit Appointment ===
    if st.button("📅 Submit Appointment"):
        st.success("Appointment submitted!")
        st.write("**Summary:**")
        st.write(f"- Customer: {selected_customer}")
        st.write(f"- Car: {selected_car}")
        st.write(f"- Date: {appointment_date.strftime('%B %d, %Y')}")
        st.write(f"- Time: {formatted_time}")
        st.write("**Services:**")
        for item in st.session_state.service_list:
            st.write(f"• {item['service']} (Mechanic: {item['mechanic']})")