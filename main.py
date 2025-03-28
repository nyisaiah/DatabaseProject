
from supabase import create_client, Client
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


user_number = st.number_input("Enter a number", 0, None, 0)

if st.button("Submit"):
    if user_number is not None:
        # Insert into Supabase database
        data, error = supabase.table("firstTable").insert({"value": user_number}).execute()

        # Check if insert was successful
        if error and error[1]:
            st.error("❌ Failed to insert data!")
        else:
            st.success(f"✅ Number {user_number} added successfully!")

records, error = supabase.table("firstTable").select("*").execute()
st.write("Hello World")
if error and error[1]:  # Check for real errors before displaying
    st.error("❌ Failed to fetch records!")
elif records:
    # Convert records to a clean DataFrame
    import pandas as pd

    df = pd.DataFrame(records[1])  # Extract the actual data from the response

    # Display the table using Streamlit's dataframe component
    st.subheader("📌 Stored Numbers")
    st.dataframe(df, hide_index=True, use_container_width=True)