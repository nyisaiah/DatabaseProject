from .supabase_client import supabase

def get_customers():
    response = supabase.table("customers").select('*').order("custlname").execute()
    return response.data

def add_customer(fName, lName, phoneNumber):
    response = supabase.table("customers").insert({
        "custfname":fName,
        "custlname":lName,
        "custphonenumber":phoneNumber
        }).execute()
    return response

def cust_with_car(customer: int, car: int):
    try:
        supabase.rpc("associate_customer", {'cust_id': customer, 'car_id': car}).execute()
        return 1
    except Exception as e:
        print(e)
        return 0