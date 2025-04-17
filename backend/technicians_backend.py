from .supabase_client import supabase

def add_technician(fname, lname):
    response = supabase.table('technicians').insert({
        'techfname': fname,
        'techlname': lname
        }).execute()
    return response

def get_technicians():
    response = supabase.table("technicians").select('*').order('techlname').execute()
    return response.data

def tech_with_service(tech : int, service : int):
     response = supabase.table("tech_to_serv").insert({
        "techid":tech,
        "serviceid":service
        }).execute()
     return response