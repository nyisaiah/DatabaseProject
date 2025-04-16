import streamlit as st
from datetime import datetime, time

def render():
    st.title("🛠️ Create a Mechanic Appointment")

    # === STEP 1: Select Customer ===
    st.subheader("Step 1: Select Customer")
    customers = [
        {"id": 1, "first_name": "John", "last_name": "Doe"},
        {"id": 2, "first_name": "Jane", "last_name": "Smith"},
    ]
    customer_options = [f"{c['id']}: {c['first_name']} {c['last_name']}" for c in customers]
    selected_customer = st.selectbox("Choose a customer", [""] + customer_options)

    if selected_customer:
        customer_id = int(selected_customer.split(":")[0])

        # === STEP 2: Select Car ===
        st.subheader("Step 2: Select Car")
        cars = [
            {"id": 1, "plate": "ABC123", "make": "Toyota", "model": "Camry"},
            {"id": 2, "plate": "XYZ789", "make": "Honda", "model": "Civic"},
        ]
        car_options = [f"{c['id']}: {c['plate']} - {c['make']} {c['model']}" for c in cars]
        selected_car = st.selectbox("Choose a car", [""] + car_options)

        if selected_car:
            car_id = int(selected_car.split(":")[0])

            # === STEP 3: Select Date and Time ===
            st.subheader("Step 3: Select Date and Time")
            appointment_date = st.date_input("Appointment Date", None)
            appointment_time = st.time_input("Appointment Time", value=("hh:mm"))
            formatted_time = appointment_time.strftime("%I:%M %p")

            if appointment_time and appointment_date:
                    # === STEP 4: Assign Technician and Add Services ===
                st.subheader("Step 4: Assign Technician and Add Services")

                # Placeholder data
                technicians = [
                    {"id": 1, "name": "Mike"},
                    {"id": 2, "name": "Linda"},
                    {"id": 3, "name": "Carlos"},
                ]

                # This would come from a backend function like get_services_for_tech(tech_id)
                tech_services_map = {
                    1: ["Oil Change", "Brake Inspection"],  # Mike
                    2: ["Tire Rotation"],                   # Linda
                    3: ["Oil Change", "Tire Rotation"]      # Carlos
                }

                if "service_list" not in st.session_state:
                    st.session_state.service_list = []

                tech_options = [f"{t['id']}: {t['name']}" for t in technicians]
                selected_tech = st.selectbox("Select Technician", tech_options)

                if selected_tech:
                    tech_id = int(selected_tech.split(":")[0])
                    available_services = tech_services_map.get(tech_id, [])

                    if available_services:
                        with st.form(key="service_form"):
                            selected_service = st.selectbox("Select a service this tech will do", available_services)
                            add_service = st.form_submit_button("➕ Add Service")

                            # Prevent duplicates
                            existing_services = [item["service"] for item in st.session_state.service_list]
                            if add_service:
                                if selected_service in existing_services:
                                    st.warning(f"{selected_service} already added.")
                                else:
                                    st.session_state.service_list.append({
                                        "service": selected_service,
                                        "mechanic": selected_tech.split(": ")[1]
                                    })
                                    st.success(f"{selected_service} added with {selected_tech.split(': ')[1]}")
                    else:
                        st.warning("This technician is not assigned to any services.")

                # === Show Services Added with Remove Buttons ===
                if st.session_state.service_list:
                    st.write("### Services Added:")
                    for idx, item in enumerate(st.session_state.service_list):
                        col1, col2, col3 = st.columns([4, 4, 1])
                        with col1:
                            st.write(f"{item['service']}")
                        with col2:
                            st.write(f"Mechanic: {item['mechanic']}")
                        with col3:
                            if st.button("❌", key=f"remove_{idx}"):
                                st.session_state.service_list.pop(idx)
                                st.rerun()

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