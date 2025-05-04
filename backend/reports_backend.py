from .supabase_client import supabase
from datetime import date, time
import pandas as pd

def get_jobs_for_day(date: date):
    response = supabase.rpc("get_jobs_for_date", {'target_date': date.isoformat()}).execute()
    return response.data


def get_services_within_time(service: str,date1: date, date2: date):
    response = supabase.table(
        "all_data").select(
            'servicename',
            'apptdate', 
            'job_time').eq(
                'servicename', 
                service).gte(
                    'apptdate',
                    date1).lte(
                        'apptdate',
                        date2).order('apptdate').execute()
    return response.data

def get_total_price(date1: date, date2: date):
    response = supabase.rpc("get_total_price", {'date1': date1.isoformat(), 'date2':date2.isoformat()}).execute()
    return response.data


def get_jobs_for_tech(tech: int, date1: date, date2: date):
    response = supabase.rpc("get_services_by_tech",{'tech_id': tech, 'start_date': date1.isoformat(), 'end_date': date2.isoformat()}).execute()
    return response.data



def get_services_for_car(customer: int):
    response = supabase.rpc("get_services_history",{'customer': customer}).execute()
    return response.data

# json_list = get_services_for_car(2)
# df = pd.DataFrame(json_list)
# print(df)

def get_techs_no_work():
    response = supabase.rpc('get_techs_without_jobs').execute()
    return response.data

json_list = get_techs_no_work()
df = pd.DataFrame(json_list)
print(df)