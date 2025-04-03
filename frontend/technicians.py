import streamlit as st

def render():
    st.title("🧑‍🔧 Technicians Page")

    st.subheader("🔍 View Technicians")
    if st.button("Load Technicians"):
        st.info("Would display all technicians.")

    st.subheader("➕ Add Technician")
    with st.form("add_tech"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        submitted = st.form_submit_button("Add")
        if submitted:
            st.success("Technician would be added.")

    st.subheader("🔗 Associate Technician with Service")

    tech_list = ["5: Mike Johnson", "6: Linda Lee"]
    service_list = ["101: Oil Change", "102: Tire Rotation"]

    with st.form("link_tech_service"):
        selected_tech = st.selectbox("Select Technician", tech_list)
        selected_service = st.selectbox("Select Service", service_list)
        linked = st.form_submit_button("Link")
        if linked:
            st.success(f"Linked {selected_tech} with {selected_service}.")