import streamlit as st

def render():
    st.title("🧾 Services Page")

    st.subheader("🔍 View Services")
    if st.button("Load Services"):
        st.info("Would display all available services.")

    st.subheader("➕ Add Service")
    with st.form("add_service"):
        name = st.text_input("Service Name")
        price = st.number_input("Service Price", min_value=0.0, step=1.0)
        submitted = st.form_submit_button("Add")
        if submitted:
            st.success("Service would be added.")

    st.subheader("🔗 Associate Service with Technician")

    service_list = ["101: Oil Change", "102: Tire Rotation"]
    tech_list = ["5: Mike Johnson", "6: Linda Lee"]

    with st.form("link_service_tech"):
        selected_service = st.selectbox("Select Service", service_list)
        selected_tech = st.selectbox("Select Technician", tech_list)
        linked = st.form_submit_button("Link")
        if linked:
            st.success(f"Linked {selected_service} with {selected_tech}.")