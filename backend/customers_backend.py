from .supabase_client import supabase

def get_customers():
    response = supabase.table("customers").select('*').execute()
    return response.data

def add_customer(fName, lName, phoneNumber):
    response = supabase.table("customers").insert({
        "custfname":fName,
        "custlname":lName,
        "custphonenumber":phoneNumber
        }).execute()
    return response
    