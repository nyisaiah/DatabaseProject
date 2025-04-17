from .supabase_client import supabase
import pandas as pd
from datetime import date, time


def get_ownership(customer : int):
    response = supabase.table(
        'ownership_full_info').select(
            'ownership_id',
            'car_id', 
            'licenseplate',
            'makename',
            'modelname').eq('cust_id', customer).order('makename').execute()
    return response.data

def get_tech_to_service(tech : int):
    response = supabase.table(
        'tech_service_full_info').select(
        'id', 
        'servicename',
        'serviceprice').eq('techid', tech).order('servicename').execute()
    return response.data
    
def add_appointment(date: date, time: time, ownership_id):
    data = {
        'apptdate': date.isoformat(),                    
        'appttime': time.strftime('%H:%M:%S'),          
        'ownership': ownership_id
    }
    response = supabase.table('appointments').insert(data).execute()
    if response.data and len(response.data) > 0:
        return response.data[0]['apptid']
    else:
        print("❌ Insert failed or no data returned:", response)
        return None


def add_job(appt_id, job_id):

    data = {
        'appt_id': appt_id,
        'tech_to_serv_id': job_id
    }

    try:
        response = supabase.table('jobs_appointment').insert(data).execute()
        print("✅ Job inserted successfully:", response.data)
        return response
    except Exception as e:
        print("❌ Supabase insert error caught!")
        return None