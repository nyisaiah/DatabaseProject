from .supabase_client import supabase

def add_service(name, price):
    supabase.table('services').insert({
        'servicename': name,
        'serviceprice': price
        }).execute()

def get_services():
    response = supabase.table("services").select('*').order('servicename').execute()
    return response.data
