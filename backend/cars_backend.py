from .supabase_client import supabase
import pandas as pd


def get_cars():
    response = supabase.table("car_full_info").select('*').order('makename').order('modelname').execute()
    return response.data

df = pd.DataFrame(get_cars())
print(df)

