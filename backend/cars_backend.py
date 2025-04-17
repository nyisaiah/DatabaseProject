from .supabase_client import supabase
import pandas as pd


def get_cars():
    response = supabase.table("car_full_info").select('*').order('makename').order('modelname').execute()
    return response.data

def get_makes():
    response = supabase.table("make").select('*').order('makename').execute()
    return response.data

def get_models(makeid):
    response = supabase.schema("public").table("model").select('*').eq('makeid',makeid).order('modelname').execute()
    return response.data

def add_car(licenseplate, makeid, modelid):
    data = {
        "licenseplate": licenseplate,
        "makeid": makeid,
        "modelid": modelid
    }
    response = supabase.table("cars").insert(data).execute()
    return response

df = pd.DataFrame(get_cars())
print(df)

